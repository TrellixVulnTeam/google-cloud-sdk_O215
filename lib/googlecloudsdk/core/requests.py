# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A module to get an unauthenticated requests.Session object."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import socket

from googlecloudsdk.core import properties
from googlecloudsdk.core import transport
from googlecloudsdk.core.util import http_proxy_types

import requests
import six
from six.moves import urllib
import socks


def GetSession(timeout='unset', response_encoding=None, ca_certs=None):
  """Get a requests.Session that is properly configured for use by gcloud.

  This method does not add credentials to the client. For a requests.Session
  that has been authenticated, use core.credentials.requests.GetSession().

  Args:
    timeout: double, The timeout in seconds. This is the
        socket level timeout. If timeout is None, timeout is infinite. If
        default argument 'unset' is given, a sensible default is selected using
        transport.GetDefaultTimeout().
    response_encoding: str, the encoding to decode with when accessing
        response.text. If none, then the encoding will be inferred from the
        response.
    ca_certs: str, absolute filename of a ca_certs file that overrides the
        default. The gcloud config property for ca_certs, in turn, overrides
        this argument.

  Returns:
    A requests.Session object configured with all the required settings
    for gcloud.
  """
  http_client = _CreateRawSession(timeout, ca_certs)
  http_client = RequestWrapper().WrapWithDefaults(http_client,
                                                  response_encoding)
  return http_client


class HTTPAdapter(requests.adapters.HTTPAdapter):
  """Transport adapter for requests.

  Transport adapters provide an interface to extend the default behavior of the
  requests library using the full power of the underlying urrlib3 library.

  See https://requests.readthedocs.io/en/master/user/advanced/
      #transport-adapters for more information about adapters.

  Attributes:
    rdns: If True, DNS queries will not be performed locally, and instead handed
        to the proxy to resolve.
  """

  def __init__(self, rdns, *args, **kwargs):
    self.rdns = rdns
    super(HTTPAdapter, self).__init__(*args, **kwargs)

  def send(self, request, **kwargs):
    if not self.rdns:
      connection_pool_kwargs = self.poolmanager.connection_pool_kw

      result = urllib.parse.urlparse(request.url)
      # Resolve DNS locally using first IP
      resolved_ip = socket.getaddrinfo(result.hostname, None)[0][4][0]

      request.url = request.url.replace(result.hostname, resolved_ip, 1)
      connection_pool_kwargs['server_hostname'] = result.hostname  # SNI
      connection_pool_kwargs['assert_hostname'] = result.hostname

      # overwrite the host header
      request.headers['Host'] = result.hostname

    return super(HTTPAdapter, self).send(request, **kwargs)


def GetProxyInfo():
  """Returns the proxy string for use by requests from gcloud properties.

  See https://requests.readthedocs.io/en/master/user/advanced/#proxies.
  """
  proxy_type = properties.VALUES.proxy.proxy_type.Get()
  proxy_address = properties.VALUES.proxy.address.Get()
  proxy_port = properties.VALUES.proxy.port.GetInt()

  proxy_prop_set = len(
      [f for f in (proxy_type, proxy_address, proxy_port) if f])
  if proxy_prop_set > 0 and proxy_prop_set != 3:
    raise properties.InvalidValueError(
        'Please set all or none of the following properties: '
        'proxy/type, proxy/address and proxy/port')

  if not proxy_prop_set:
    return

  proxy_rdns = properties.VALUES.proxy.rdns.GetBool()
  proxy_user = properties.VALUES.proxy.username.Get()
  proxy_pass = properties.VALUES.proxy.password.Get()

  proxy_type = http_proxy_types.PROXY_TYPE_MAP[proxy_type]
  if proxy_type == socks.PROXY_TYPE_SOCKS4:
    proxy_scheme = 'socks4a' if proxy_rdns else 'socks4'
  elif proxy_type == socks.PROXY_TYPE_SOCKS5:
    proxy_scheme = 'socks5h' if proxy_rdns else 'socks5'
  elif proxy_type == socks.PROXY_TYPE_HTTP:
    proxy_scheme = 'https'
  elif proxy_type == socks.PROXY_TYPE_HTTP_NO_TUNNEL:
    proxy_scheme = 'http'
  else:
    raise ValueError('Unsupported proxy type: {}'.format(proxy_type))

  if proxy_user or proxy_pass:
    proxy_auth = ':'.join(x or '' for x in (proxy_user, proxy_pass))
    proxy_auth += '@'
  else:
    proxy_auth = ''
  return '{}://{}{}:{}'.format(proxy_scheme, proxy_auth, proxy_address,
                               proxy_port)


def Session(
    timeout=None,
    ca_certs=None,
    disable_ssl_certificate_validation=False):
  """Returns a requests.Session subclass.

  Args:
    timeout: float, Request timeout, in seconds.
    ca_certs: str, absolute filename of a ca_certs file
    disable_ssl_certificate_validation: bool, If true, disable ssl certificate
        validation.

  Returns: A requests.Session subclass.
  """
  session = _Session(timeout=timeout)

  proxy_rdns = True
  proxy_info = GetProxyInfo()
  if proxy_info:
    proxy_rdns = properties.VALUES.proxy.rdns.GetBool()
    session.proxies = {
        'http': proxy_info,
        'https': proxy_info,
    }
  adapter = HTTPAdapter(proxy_rdns)

  if disable_ssl_certificate_validation:
    session.verify = False
  elif ca_certs:
    session.verify = ca_certs

  # TODO(b/157164006) - Support mTLS
  session.mount('https://', adapter)
  return session


def _CreateRawSession(timeout='unset', ca_certs=None):
  """Create a requests.Session matching the appropriate gcloud properties."""
  # Compared with setting the default timeout in the function signature (i.e.
  # timeout=300), this lets you test with short default timeouts by mocking
  # GetDefaultTimeout.
  if timeout != 'unset':
    effective_timeout = timeout
  else:
    effective_timeout = transport.GetDefaultTimeout()

  no_validate = properties.VALUES.auth.disable_ssl_validation.GetBool() or False
  ca_certs_property = properties.VALUES.core.custom_ca_certs_file.Get()
  # Believe an explicitly-set ca_certs property over anything we added.
  if ca_certs_property:
    ca_certs = ca_certs_property
  if no_validate:
    ca_certs = None
  return Session(timeout=effective_timeout,
                 ca_certs=ca_certs,
                 disable_ssl_certificate_validation=no_validate)


def _GetURIFromRequestArgs(url, params):
  """Gets the complete URI by merging url and params from the request args."""
  url_parts = urllib.parse.urlsplit(url)
  query_params = urllib.parse.parse_qs(url_parts.query)
  for param, value in six.iteritems(params or {}):
    query_params[param] = value
  # Need to do this to convert a SplitResult into a list so it can be modified.
  url_parts = list(url_parts)
  # pylint:disable=redundant-keyword-arg, this is valid syntax for this lib
  url_parts[3] = urllib.parse.urlencode(query_params, doseq=True)

  # pylint:disable=too-many-function-args, This is just bogus.
  return urllib.parse.urlunsplit(url_parts)


class Request(transport.Request):
  """Encapsulates parameters for making a general HTTP request.

  This implementation does additional manipulation to ensure that the request
  parameters are specified in the same way as they were specified by the
  caller. That is, if the user calls:
      request('URI', 'GET', None, {'header': '1'})

  After modifying the request, we will call request using positional
  parameters, instead of transforming the request into:
      request('URI', method='GET', body=None, headers={'header': '1'})
  """

  @classmethod
  def FromRequestArgs(cls, *args, **kwargs):
    return cls(*args, **kwargs)

  def __init__(self, method, url, params=None, data=None, headers=None,
               **kwargs):
    self._kwargs = kwargs
    uri = _GetURIFromRequestArgs(url, params)
    super(Request, self).__init__(uri, method, headers or {}, data)

  def ToRequestArgs(self):
    args = [self.method, self.uri]
    kwargs = dict(self._kwargs)
    kwargs['headers'] = self.headers
    if self.body:
      kwargs['data'] = self.body
    return args, kwargs


class Response(transport.Response):
  """Encapsulates responses from making a general HTTP request."""

  @classmethod
  def FromResponse(cls, response):
    return cls(response.status_code, response.headers, response.content)


class RequestWrapper(transport.RequestWrapper):
  """Class for wrapping request.Session requests."""

  request_class = Request
  response_class = Response

  def DecodeResponse(self, response, response_encoding):
    response.encoding = response_encoding
    return response


class _Session(requests.Session):
  """Base request.Session class."""

  def __init__(self, timeout):
    super(_Session, self).__init__()
    self.timeout = timeout

  def request(self, *args, **kwargs):
    if 'timeout' not in kwargs:
      kwargs['timeout'] = self.timeout

    return super(_Session, self).request(*args, **kwargs)
