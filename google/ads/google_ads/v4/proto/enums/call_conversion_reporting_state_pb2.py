# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/enums/call_conversion_reporting_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/enums/call_conversion_reporting_state.proto',
  package='google.ads.googleads.v4.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v4.enumsB!CallConversionReportingStateProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V4.Enums\312\002\035Google\\Ads\\GoogleAds\\V4\\Enums\352\002!Google::Ads::GoogleAds::V4::Enums'),
  serialized_pb=_b('\nIgoogle/ads/googleads_v4/proto/enums/call_conversion_reporting_state.proto\x12\x1dgoogle.ads.googleads.v4.enums\x1a\x1cgoogle/api/annotations.proto\"\xcc\x01\n CallConversionReportingStateEnum\"\xa7\x01\n\x1c\x43\x61llConversionReportingState\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12,\n(USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION\x10\x03\x12-\n)USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION\x10\x04\x42\xf6\x01\n!com.google.ads.googleads.v4.enumsB!CallConversionReportingStateProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v4/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V4.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V4\\Enums\xea\x02!Google::Ads::GoogleAds::V4::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CALLCONVERSIONREPORTINGSTATEENUM_CALLCONVERSIONREPORTINGSTATE = _descriptor.EnumDescriptor(
  name='CallConversionReportingState',
  full_name='google.ads.googleads.v4.enums.CallConversionReportingStateEnum.CallConversionReportingState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=176,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_CALLCONVERSIONREPORTINGSTATEENUM_CALLCONVERSIONREPORTINGSTATE)


_CALLCONVERSIONREPORTINGSTATEENUM = _descriptor.Descriptor(
  name='CallConversionReportingStateEnum',
  full_name='google.ads.googleads.v4.enums.CallConversionReportingStateEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CALLCONVERSIONREPORTINGSTATEENUM_CALLCONVERSIONREPORTINGSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=343,
)

_CALLCONVERSIONREPORTINGSTATEENUM_CALLCONVERSIONREPORTINGSTATE.containing_type = _CALLCONVERSIONREPORTINGSTATEENUM
DESCRIPTOR.message_types_by_name['CallConversionReportingStateEnum'] = _CALLCONVERSIONREPORTINGSTATEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CallConversionReportingStateEnum = _reflection.GeneratedProtocolMessageType('CallConversionReportingStateEnum', (_message.Message,), dict(
  DESCRIPTOR = _CALLCONVERSIONREPORTINGSTATEENUM,
  __module__ = 'google.ads.googleads_v4.proto.enums.call_conversion_reporting_state_pb2'
  ,
  __doc__ = """Container for enum describing possible data types for call conversion
  reporting state.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.enums.CallConversionReportingStateEnum)
  ))
_sym_db.RegisterMessage(CallConversionReportingStateEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)