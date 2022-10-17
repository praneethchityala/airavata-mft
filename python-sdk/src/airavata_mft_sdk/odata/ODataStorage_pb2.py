# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: odata/ODataStorage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18odata/ODataStorage.proto\x12\x34org.apache.airavata.mft.resource.stubs.odata.storage\"@\n\x0cODataStorage\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61seUrl\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"8\n\x17ODataStorageListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"p\n\x18ODataStorageListResponse\x12T\n\x08storages\x18\x01 \x03(\x0b\x32\x42.org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorage\"+\n\x16ODataStorageGetRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"M\n\x19ODataStorageCreateRequest\x12\x0f\n\x07\x62\x61seUrl\x18\x01 \x01(\t\x12\x11\n\tstorageId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"M\n\x19ODataStorageUpdateRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61seUrl\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"/\n\x1aODataStorageUpdateResponse\x12\x11\n\tstorageId\x18\x01 \x01(\t\".\n\x19ODataStorageDeleteRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\",\n\x1aODataStorageDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x42\x02P\x01\x62\x06proto3')



_ODATASTORAGE = DESCRIPTOR.message_types_by_name['ODataStorage']
_ODATASTORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['ODataStorageListRequest']
_ODATASTORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['ODataStorageListResponse']
_ODATASTORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['ODataStorageGetRequest']
_ODATASTORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['ODataStorageCreateRequest']
_ODATASTORAGEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['ODataStorageUpdateRequest']
_ODATASTORAGEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['ODataStorageUpdateResponse']
_ODATASTORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['ODataStorageDeleteRequest']
_ODATASTORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['ODataStorageDeleteResponse']
ODataStorage = _reflection.GeneratedProtocolMessageType('ODataStorage', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGE,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorage)
  })
_sym_db.RegisterMessage(ODataStorage)

ODataStorageListRequest = _reflection.GeneratedProtocolMessageType('ODataStorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGELISTREQUEST,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageListRequest)
  })
_sym_db.RegisterMessage(ODataStorageListRequest)

ODataStorageListResponse = _reflection.GeneratedProtocolMessageType('ODataStorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGELISTRESPONSE,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageListResponse)
  })
_sym_db.RegisterMessage(ODataStorageListResponse)

ODataStorageGetRequest = _reflection.GeneratedProtocolMessageType('ODataStorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGEGETREQUEST,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageGetRequest)
  })
_sym_db.RegisterMessage(ODataStorageGetRequest)

ODataStorageCreateRequest = _reflection.GeneratedProtocolMessageType('ODataStorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGECREATEREQUEST,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageCreateRequest)
  })
_sym_db.RegisterMessage(ODataStorageCreateRequest)

ODataStorageUpdateRequest = _reflection.GeneratedProtocolMessageType('ODataStorageUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGEUPDATEREQUEST,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageUpdateRequest)
  })
_sym_db.RegisterMessage(ODataStorageUpdateRequest)

ODataStorageUpdateResponse = _reflection.GeneratedProtocolMessageType('ODataStorageUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGEUPDATERESPONSE,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageUpdateResponse)
  })
_sym_db.RegisterMessage(ODataStorageUpdateResponse)

ODataStorageDeleteRequest = _reflection.GeneratedProtocolMessageType('ODataStorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGEDELETEREQUEST,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageDeleteRequest)
  })
_sym_db.RegisterMessage(ODataStorageDeleteRequest)

ODataStorageDeleteResponse = _reflection.GeneratedProtocolMessageType('ODataStorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ODATASTORAGEDELETERESPONSE,
  '__module__' : 'odata.ODataStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.odata.storage.ODataStorageDeleteResponse)
  })
_sym_db.RegisterMessage(ODataStorageDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _ODATASTORAGE._serialized_start=82
  _ODATASTORAGE._serialized_end=146
  _ODATASTORAGELISTREQUEST._serialized_start=148
  _ODATASTORAGELISTREQUEST._serialized_end=204
  _ODATASTORAGELISTRESPONSE._serialized_start=206
  _ODATASTORAGELISTRESPONSE._serialized_end=318
  _ODATASTORAGEGETREQUEST._serialized_start=320
  _ODATASTORAGEGETREQUEST._serialized_end=363
  _ODATASTORAGECREATEREQUEST._serialized_start=365
  _ODATASTORAGECREATEREQUEST._serialized_end=442
  _ODATASTORAGEUPDATEREQUEST._serialized_start=444
  _ODATASTORAGEUPDATEREQUEST._serialized_end=521
  _ODATASTORAGEUPDATERESPONSE._serialized_start=523
  _ODATASTORAGEUPDATERESPONSE._serialized_end=570
  _ODATASTORAGEDELETEREQUEST._serialized_start=572
  _ODATASTORAGEDELETEREQUEST._serialized_end=618
  _ODATASTORAGEDELETERESPONSE._serialized_start=620
  _ODATASTORAGEDELETERESPONSE._serialized_end=664
# @@protoc_insertion_point(module_scope)