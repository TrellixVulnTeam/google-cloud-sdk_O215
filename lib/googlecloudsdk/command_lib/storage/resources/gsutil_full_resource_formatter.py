# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
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
"""Gsutil-specific formatting of BucketResource and ObjectResource."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.storage.resources import full_resource_formatter as base
from googlecloudsdk.command_lib.storage.resources import shim_format_util

_BUCKET_DISPLAY_TITLES_AND_DEFAULTS = (
    base.BucketDisplayTitlesAndDefaults(
        storage_class=base.FieldDisplayTitleAndDefault(
            title='Storage class', default=None),
        location_type=base.FieldDisplayTitleAndDefault(
            title='Location type', default=None),
        # Using literal string 'None' as default so that it gets displayed
        # if the value is missing.
        location=base.FieldDisplayTitleAndDefault(
            title='Location constraint', default=shim_format_util.NONE_STRING),
        versioning_enabled=base.FieldDisplayTitleAndDefault(
            title='Versioning enabled', default=shim_format_util.NONE_STRING),
        logging_config=base.FieldDisplayTitleAndDefault(
            title='Logging configuration',
            default=shim_format_util.NONE_STRING),
        website_config=base.FieldDisplayTitleAndDefault(
            title='Website configuration',
            default=shim_format_util.NONE_STRING),
        cors_config=base.FieldDisplayTitleAndDefault(
            title='CORS configuration', default=shim_format_util.NONE_STRING),
        lifecycle_config=base.FieldDisplayTitleAndDefault(
            title='Lifecycle configuration',
            default=shim_format_util.NONE_STRING),
        requester_pays=base.FieldDisplayTitleAndDefault(
            title='Requester Pays enabled',
            default=shim_format_util.NONE_STRING),
        retention_policy=base.FieldDisplayTitleAndDefault(
            title='Retention Policy', default=None),
        default_event_based_hold=base.FieldDisplayTitleAndDefault(
            title='Default Event-Based Hold', default=None),
        labels=base.FieldDisplayTitleAndDefault(
            title='Labels', default=shim_format_util.NONE_STRING),
        default_kms_key=base.FieldDisplayTitleAndDefault(
            title='Default KMS key', default=shim_format_util.NONE_STRING),
        creation_time=base.FieldDisplayTitleAndDefault(
            title='Time created', default=None),
        update_time=base.FieldDisplayTitleAndDefault(
            title='Time updated', default=None),
        metageneration=base.FieldDisplayTitleAndDefault(
            title='Metageneration', default=None),
        bucket_policy_only_enabled=base.FieldDisplayTitleAndDefault(
            title='Bucket Policy Only enabled',
            default=None,
            field_name='_bucket_policy_only_enabled'),
        satisfies_pzs=base.FieldDisplayTitleAndDefault(
            title='Satisfies PZS', default=None),
        acl=base.FieldDisplayTitleAndDefault(
            title='ACL', default=shim_format_util.EMPTY_LIST_STRING),
        default_acl=base.FieldDisplayTitleAndDefault(
            title='Default ACL', default=None),
    ))

_OBJECT_DISPLAY_TITLES_AND_DEFAULTS = (
    base.ObjectDisplayTitlesAndDefaults(
        creation_time=base.FieldDisplayTitleAndDefault(
            title='Creation time', default=None),
        update_time=base.FieldDisplayTitleAndDefault(
            title='Update time', default=None),
        storage_class_update_time=base.FieldDisplayTitleAndDefault(
            title='Storage class update time', default=None),
        storage_class=base.FieldDisplayTitleAndDefault(
            title='Storage class', default=None),
        temporary_hold=base.FieldDisplayTitleAndDefault(
            title='Temporary Hold', default=None),
        event_based_hold=base.FieldDisplayTitleAndDefault(
            title='Event-Based Hold', default=None),
        retention_expiration=base.FieldDisplayTitleAndDefault(
            title='Retention Expiration', default=None),
        kms_key=base.FieldDisplayTitleAndDefault(title='KMS key', default=None),
        cache_control=base.FieldDisplayTitleAndDefault(
            title='Cache-Control', default=None),
        content_disposition=base.FieldDisplayTitleAndDefault(
            title='Content-Disposition', default=None),
        content_encoding=base.FieldDisplayTitleAndDefault(
            title='Content-Encoding', default=None),
        content_language=base.FieldDisplayTitleAndDefault(
            title='Content-Language', default=None),
        content_length=base.FieldDisplayTitleAndDefault(
            title='Content-Length', default=shim_format_util.NONE_STRING),
        content_type=base.FieldDisplayTitleAndDefault(
            title='Content-Type', default=shim_format_util.NONE_STRING),
        component_count=base.FieldDisplayTitleAndDefault(
            title='Component-Count', default=None),
        custom_time=base.FieldDisplayTitleAndDefault(
            title='Custom-Time', default=None),
        noncurrent_time=base.FieldDisplayTitleAndDefault(
            title='Noncurrent time', default=None),
        additional_properties=base.FieldDisplayTitleAndDefault(
            title='Metadata', default=None),
        crc32c_hash=base.FieldDisplayTitleAndDefault(
            title='Hash (crc32c)', default=None),
        md5_hash=base.FieldDisplayTitleAndDefault(
            title='Hash (md5)', default=None),
        encryption_algorithm=base.FieldDisplayTitleAndDefault(
            title='Encryption algorithm', default=None),
        encryption_key_sha256=base.FieldDisplayTitleAndDefault(
            title='Encryption key SHA256', default=None),
        etag=base.FieldDisplayTitleAndDefault(
            title='ETag', default=shim_format_util.NONE_STRING),
        generation=base.FieldDisplayTitleAndDefault(
            title='Generation', default=None),
        metageneration=base.FieldDisplayTitleAndDefault(
            title='Metageneration', default=None),
        acl=base.FieldDisplayTitleAndDefault(
            title='ACL', default=shim_format_util.EMPTY_LIST_STRING),
    ))


class GsutilFullResourceFormatter(base.FullResourceFormatter):
  """Format a resource as per gsutil Storage style for ls -L output."""

  def format_bucket(self, url, displayable_bucket_data):
    """See super class."""
    shim_format_util.replace_time_values_with_gsutil_style_strings(
        displayable_bucket_data)
    shim_format_util.replace_bucket_values_with_present_string(
        displayable_bucket_data)
    return base.get_formatted_string(url, displayable_bucket_data,
                                     _BUCKET_DISPLAY_TITLES_AND_DEFAULTS)

  def format_object(self,
                    url,
                    displayable_object_data,
                    show_acl=True,
                    show_version_in_url=False):
    """See super class."""
    shim_format_util.replace_time_values_with_gsutil_style_strings(
        displayable_object_data)
    shim_format_util.replace_object_values_with_encryption_string(
        displayable_object_data, 'encrypted')
    shim_format_util.reformat_custom_metadata_for_gsutil(
        displayable_object_data)
    return base.get_formatted_string(
        url,
        displayable_object_data,
        _OBJECT_DISPLAY_TITLES_AND_DEFAULTS,
        show_acl=show_acl,
        show_version_in_url=show_version_in_url)
