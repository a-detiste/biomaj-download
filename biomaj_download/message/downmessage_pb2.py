# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: downmessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64ownmessage.proto\x12\x0f\x62iomaj.download\"\x9d\x02\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04root\x18\x02 \x01(\t\x12\x0f\n\x07save_as\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x30\n\x08metadata\x18\x05 \x01(\x0b\x32\x1e.biomaj.download.File.MetaData\x1a\xa8\x01\n\x08MetaData\x12\x13\n\x0bpermissions\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12\r\n\x05month\x18\x06 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x07 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x08 \x01(\t\x12\x0b\n\x03md5\x18\t \x01(\t\x12\x15\n\rdownload_time\x18\n \x01(\x03\"0\n\x08\x46ileList\x12$\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x15.biomaj.download.File\"\xaa\x02\n\tOperation\x12\x32\n\x04type\x18\x01 \x02(\x0e\x32$.biomaj.download.Operation.OPERATION\x12/\n\x08\x64ownload\x18\x02 \x01(\x0b\x32\x1d.biomaj.download.DownloadFile\x12)\n\x07process\x18\x03 \x01(\x0b\x32\x18.biomaj.download.Process\x12/\n\x05trace\x18\x04 \x01(\x0b\x32 .biomaj.download.Operation.Trace\x1a*\n\x05Trace\x12\x10\n\x08trace_id\x18\x01 \x02(\t\x12\x0f\n\x07span_id\x18\x02 \x02(\t\"0\n\tOPERATION\x12\x08\n\x04LIST\x10\x00\x12\x0c\n\x08\x44OWNLOAD\x10\x01\x12\x0b\n\x07PROCESS\x10\x02\"\x17\n\x07Process\x12\x0c\n\x04\x65xec\x18\x01 \x02(\t\"\x94\x0b\n\x0c\x44ownloadFile\x12\x0c\n\x04\x62\x61nk\x18\x01 \x02(\t\x12\x0f\n\x07session\x18\x02 \x02(\t\x12\x11\n\tlocal_dir\x18\x03 \x02(\t\x12\x18\n\x10timeout_download\x18\x04 \x01(\x05\x12=\n\x0bremote_file\x18\x05 \x02(\x0b\x32(.biomaj.download.DownloadFile.RemoteFile\x12\x32\n\x05proxy\x18\x06 \x01(\x0b\x32#.biomaj.download.DownloadFile.Proxy\x12\x43\n\x0bhttp_method\x18\x08 \x01(\x0e\x32).biomaj.download.DownloadFile.HTTP_METHOD:\x03GET\x12;\n\x07options\x18\t \x03(\x0b\x32*.biomaj.download.DownloadFile.OptionsEntry\x1a$\n\x05Param\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x1a\xcd\x03\n\tHttpParse\x12\x91\x01\n\x08\x64ir_line\x18\x01 \x02(\t:\x7f<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[DIR\\]\"[\\s]*/?>[\\s]*<a[\\s]+href=\"([\\S]+)/\"[\\s]*>.*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})\x12\xa5\x01\n\tfile_line\x18\x02 \x02(\t:\x91\x01<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[[\\s]+\\]\"[\\s]*/?>[\\s]<a[\\s]+href=\"([\\S]+)\".*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})[\\s]+([\\d\\.]+[MKG]{0,1})\x12\x13\n\x08\x64ir_name\x18\x03 \x02(\x05:\x01\x31\x12\x13\n\x08\x64ir_date\x18\x04 \x02(\x05:\x01\x32\x12\x14\n\tfile_name\x18\x05 \x02(\x05:\x01\x31\x12\x14\n\tfile_date\x18\x06 \x02(\x05:\x01\x32\x12\x18\n\x10\x66ile_date_format\x18\x07 \x01(\t\x12\x14\n\tfile_size\x18\x08 \x02(\x05:\x01\x33\x1a\xb8\x02\n\nRemoteFile\x12$\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x15.biomaj.download.File\x12\x38\n\x08protocol\x18\x02 \x02(\x0e\x32&.biomaj.download.DownloadFile.Protocol\x12\x0e\n\x06server\x18\x03 \x02(\t\x12\x12\n\nremote_dir\x18\x04 \x02(\t\x12\x0f\n\x07save_as\x18\x05 \x01(\t\x12\x32\n\x05param\x18\x06 \x03(\x0b\x32#.biomaj.download.DownloadFile.Param\x12;\n\nhttp_parse\x18\x07 \x01(\x0b\x32\'.biomaj.download.DownloadFile.HttpParse\x12\x13\n\x0b\x63redentials\x18\x08 \x01(\t\x12\x0f\n\x07matches\x18\t \x03(\t\x1a*\n\x05Proxy\x12\r\n\x05proxy\x18\x01 \x02(\t\x12\x12\n\nproxy_auth\x18\x02 \x01(\t\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x93\x01\n\x08Protocol\x12\x07\n\x03\x46TP\x10\x00\x12\x08\n\x04\x46TPS\x10\x01\x12\x08\n\x04HTTP\x10\x02\x12\t\n\x05HTTPS\x10\x03\x12\r\n\tDIRECTFTP\x10\x04\x12\x0e\n\nDIRECTHTTP\x10\x05\x12\x0f\n\x0b\x44IRECTHTTPS\x10\x06\x12\t\n\x05LOCAL\x10\x07\x12\t\n\x05RSYNC\x10\x08\x12\t\n\x05IRODS\x10\t\x12\x0e\n\nDIRECTFTPS\x10\n\" \n\x0bHTTP_METHOD\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01')



_FILE = DESCRIPTOR.message_types_by_name['File']
_FILE_METADATA = _FILE.nested_types_by_name['MetaData']
_FILELIST = DESCRIPTOR.message_types_by_name['FileList']
_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
_OPERATION_TRACE = _OPERATION.nested_types_by_name['Trace']
_PROCESS = DESCRIPTOR.message_types_by_name['Process']
_DOWNLOADFILE = DESCRIPTOR.message_types_by_name['DownloadFile']
_DOWNLOADFILE_PARAM = _DOWNLOADFILE.nested_types_by_name['Param']
_DOWNLOADFILE_HTTPPARSE = _DOWNLOADFILE.nested_types_by_name['HttpParse']
_DOWNLOADFILE_REMOTEFILE = _DOWNLOADFILE.nested_types_by_name['RemoteFile']
_DOWNLOADFILE_PROXY = _DOWNLOADFILE.nested_types_by_name['Proxy']
_DOWNLOADFILE_OPTIONSENTRY = _DOWNLOADFILE.nested_types_by_name['OptionsEntry']
_OPERATION_OPERATION = _OPERATION.enum_types_by_name['OPERATION']
_DOWNLOADFILE_PROTOCOL = _DOWNLOADFILE.enum_types_by_name['Protocol']
_DOWNLOADFILE_HTTP_METHOD = _DOWNLOADFILE.enum_types_by_name['HTTP_METHOD']
File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {

  'MetaData' : _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), {
    'DESCRIPTOR' : _FILE_METADATA,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.File.MetaData)
    })
  ,
  'DESCRIPTOR' : _FILE,
  '__module__' : 'downmessage_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.download.File)
  })
_sym_db.RegisterMessage(File)
_sym_db.RegisterMessage(File.MetaData)

FileList = _reflection.GeneratedProtocolMessageType('FileList', (_message.Message,), {
  'DESCRIPTOR' : _FILELIST,
  '__module__' : 'downmessage_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.download.FileList)
  })
_sym_db.RegisterMessage(FileList)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {

  'Trace' : _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
    'DESCRIPTOR' : _OPERATION_TRACE,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.Operation.Trace)
    })
  ,
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'downmessage_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.download.Operation)
  })
_sym_db.RegisterMessage(Operation)
_sym_db.RegisterMessage(Operation.Trace)

Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), {
  'DESCRIPTOR' : _PROCESS,
  '__module__' : 'downmessage_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.download.Process)
  })
_sym_db.RegisterMessage(Process)

DownloadFile = _reflection.GeneratedProtocolMessageType('DownloadFile', (_message.Message,), {

  'Param' : _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
    'DESCRIPTOR' : _DOWNLOADFILE_PARAM,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.DownloadFile.Param)
    })
  ,

  'HttpParse' : _reflection.GeneratedProtocolMessageType('HttpParse', (_message.Message,), {
    'DESCRIPTOR' : _DOWNLOADFILE_HTTPPARSE,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.DownloadFile.HttpParse)
    })
  ,

  'RemoteFile' : _reflection.GeneratedProtocolMessageType('RemoteFile', (_message.Message,), {
    'DESCRIPTOR' : _DOWNLOADFILE_REMOTEFILE,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.DownloadFile.RemoteFile)
    })
  ,

  'Proxy' : _reflection.GeneratedProtocolMessageType('Proxy', (_message.Message,), {
    'DESCRIPTOR' : _DOWNLOADFILE_PROXY,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.DownloadFile.Proxy)
    })
  ,

  'OptionsEntry' : _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOWNLOADFILE_OPTIONSENTRY,
    '__module__' : 'downmessage_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.download.DownloadFile.OptionsEntry)
    })
  ,
  'DESCRIPTOR' : _DOWNLOADFILE,
  '__module__' : 'downmessage_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.download.DownloadFile)
  })
_sym_db.RegisterMessage(DownloadFile)
_sym_db.RegisterMessage(DownloadFile.Param)
_sym_db.RegisterMessage(DownloadFile.HttpParse)
_sym_db.RegisterMessage(DownloadFile.RemoteFile)
_sym_db.RegisterMessage(DownloadFile.Proxy)
_sym_db.RegisterMessage(DownloadFile.OptionsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOWNLOADFILE_OPTIONSENTRY._options = None
  _DOWNLOADFILE_OPTIONSENTRY._serialized_options = b'8\001'
  _FILE._serialized_start=39
  _FILE._serialized_end=324
  _FILE_METADATA._serialized_start=156
  _FILE_METADATA._serialized_end=324
  _FILELIST._serialized_start=326
  _FILELIST._serialized_end=374
  _OPERATION._serialized_start=377
  _OPERATION._serialized_end=675
  _OPERATION_TRACE._serialized_start=583
  _OPERATION_TRACE._serialized_end=625
  _OPERATION_OPERATION._serialized_start=627
  _OPERATION_OPERATION._serialized_end=675
  _PROCESS._serialized_start=677
  _PROCESS._serialized_end=700
  _DOWNLOADFILE._serialized_start=703
  _DOWNLOADFILE._serialized_end=2131
  _DOWNLOADFILE_PARAM._serialized_start=1040
  _DOWNLOADFILE_PARAM._serialized_end=1076
  _DOWNLOADFILE_HTTPPARSE._serialized_start=1079
  _DOWNLOADFILE_HTTPPARSE._serialized_end=1540
  _DOWNLOADFILE_REMOTEFILE._serialized_start=1543
  _DOWNLOADFILE_REMOTEFILE._serialized_end=1855
  _DOWNLOADFILE_PROXY._serialized_start=1857
  _DOWNLOADFILE_PROXY._serialized_end=1899
  _DOWNLOADFILE_OPTIONSENTRY._serialized_start=1901
  _DOWNLOADFILE_OPTIONSENTRY._serialized_end=1947
  _DOWNLOADFILE_PROTOCOL._serialized_start=1950
  _DOWNLOADFILE_PROTOCOL._serialized_end=2097
  _DOWNLOADFILE_HTTP_METHOD._serialized_start=2099
  _DOWNLOADFILE_HTTP_METHOD._serialized_end=2131
# @@protoc_insertion_point(module_scope)
