# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: http/HTTPStorage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16http/HTTPStorage.proto\x12\x33org.apache.airavata.mft.resource.stubs.http.storage\"?\n\x0bHTTPStorage\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61seUrl\x18\x03 \x01(\t\"7\n\x16HTTPStorageListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"m\n\x17HTTPStorageListResponse\x12R\n\x08storages\x18\x01 \x03(\x0b\x32@.org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorage\"*\n\x15HTTPStorageGetRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"9\n\x18HTTPStorageCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61seUrl\x18\x02 \x01(\t\"L\n\x18HTTPStorageUpdateRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61seUrl\x18\x03 \x01(\t\".\n\x19HTTPStorageUpdateResponse\x12\x11\n\tstorageId\x18\x01 \x01(\t\"-\n\x18HTTPStorageDeleteRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"+\n\x19HTTPStorageDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x42\x02P\x01\x62\x06proto3')



_HTTPSTORAGE = DESCRIPTOR.message_types_by_name['HTTPStorage']
_HTTPSTORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['HTTPStorageListRequest']
_HTTPSTORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['HTTPStorageListResponse']
_HTTPSTORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['HTTPStorageGetRequest']
_HTTPSTORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['HTTPStorageCreateRequest']
_HTTPSTORAGEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['HTTPStorageUpdateRequest']
_HTTPSTORAGEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['HTTPStorageUpdateResponse']
_HTTPSTORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['HTTPStorageDeleteRequest']
_HTTPSTORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['HTTPStorageDeleteResponse']
HTTPStorage = _reflection.GeneratedProtocolMessageType('HTTPStorage', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGE,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorage)
  })
_sym_db.RegisterMessage(HTTPStorage)

HTTPStorageListRequest = _reflection.GeneratedProtocolMessageType('HTTPStorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGELISTREQUEST,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageListRequest)
  })
_sym_db.RegisterMessage(HTTPStorageListRequest)

HTTPStorageListResponse = _reflection.GeneratedProtocolMessageType('HTTPStorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGELISTRESPONSE,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageListResponse)
  })
_sym_db.RegisterMessage(HTTPStorageListResponse)

HTTPStorageGetRequest = _reflection.GeneratedProtocolMessageType('HTTPStorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGEGETREQUEST,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageGetRequest)
  })
_sym_db.RegisterMessage(HTTPStorageGetRequest)

HTTPStorageCreateRequest = _reflection.GeneratedProtocolMessageType('HTTPStorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGECREATEREQUEST,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageCreateRequest)
  })
_sym_db.RegisterMessage(HTTPStorageCreateRequest)

HTTPStorageUpdateRequest = _reflection.GeneratedProtocolMessageType('HTTPStorageUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGEUPDATEREQUEST,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageUpdateRequest)
  })
_sym_db.RegisterMessage(HTTPStorageUpdateRequest)

HTTPStorageUpdateResponse = _reflection.GeneratedProtocolMessageType('HTTPStorageUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGEUPDATERESPONSE,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageUpdateResponse)
  })
_sym_db.RegisterMessage(HTTPStorageUpdateResponse)

HTTPStorageDeleteRequest = _reflection.GeneratedProtocolMessageType('HTTPStorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGEDELETEREQUEST,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageDeleteRequest)
  })
_sym_db.RegisterMessage(HTTPStorageDeleteRequest)

HTTPStorageDeleteResponse = _reflection.GeneratedProtocolMessageType('HTTPStorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTORAGEDELETERESPONSE,
  '__module__' : 'http.HTTPStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.http.storage.HTTPStorageDeleteResponse)
  })
_sym_db.RegisterMessage(HTTPStorageDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _HTTPSTORAGE._serialized_start=79
  _HTTPSTORAGE._serialized_end=142
  _HTTPSTORAGELISTREQUEST._serialized_start=144
  _HTTPSTORAGELISTREQUEST._serialized_end=199
  _HTTPSTORAGELISTRESPONSE._serialized_start=201
  _HTTPSTORAGELISTRESPONSE._serialized_end=310
  _HTTPSTORAGEGETREQUEST._serialized_start=312
  _HTTPSTORAGEGETREQUEST._serialized_end=354
  _HTTPSTORAGECREATEREQUEST._serialized_start=356
  _HTTPSTORAGECREATEREQUEST._serialized_end=413
  _HTTPSTORAGEUPDATEREQUEST._serialized_start=415
  _HTTPSTORAGEUPDATEREQUEST._serialized_end=491
  _HTTPSTORAGEUPDATERESPONSE._serialized_start=493
  _HTTPSTORAGEUPDATERESPONSE._serialized_end=539
  _HTTPSTORAGEDELETEREQUEST._serialized_start=541
  _HTTPSTORAGEDELETEREQUEST._serialized_end=586
  _HTTPSTORAGEDELETERESPONSE._serialized_start=588
  _HTTPSTORAGEDELETERESPONSE._serialized_end=631
# @@protoc_insertion_point(module_scope)