# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_testauth_api import paps_pb2 as grpc__testauth__api_dot_paps__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nmain.proto\x1a\x1cgrpc_testauth_api/paps.proto2h\n\x06\x46leets\x12^\n\x19GetUserStatsByCorporation\x12!.GetUserStatsByCorporationRequest\x1a\x1c.UserFleetParticipationStats0\x01\x62\x06proto3')
  ,
  dependencies=[grpc__testauth__api_dot_paps__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FLEETS = _descriptor.ServiceDescriptor(
  name='Fleets',
  full_name='Fleets',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=44,
  serialized_end=148,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserStatsByCorporation',
    full_name='Fleets.GetUserStatsByCorporation',
    index=0,
    containing_service=None,
    input_type=grpc__testauth__api_dot_paps__pb2._GETUSERSTATSBYCORPORATIONREQUEST,
    output_type=grpc__testauth__api_dot_paps__pb2._USERFLEETPARTICIPATIONSTATS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLEETS)

DESCRIPTOR.services_by_name['Fleets'] = _FLEETS

# @@protoc_insertion_point(module_scope)
