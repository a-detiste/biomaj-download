# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: downmessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64ownmessage.proto\x12\x0f\x62iomaj.download\"\x9d\x02\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04root\x18\x02 \x01(\t\x12\x0f\n\x07save_as\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x30\n\x08metadata\x18\x05 \x01(\x0b\x32\x1e.biomaj.download.File.MetaData\x1a\xa8\x01\n\x08MetaData\x12\x13\n\x0bpermissions\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12\r\n\x05month\x18\x06 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x07 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x08 \x01(\t\x12\x0b\n\x03md5\x18\t \x01(\t\x12\x15\n\rdownload_time\x18\n \x01(\x03\"0\n\x08\x46ileList\x12$\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x15.biomaj.download.File\"\xaa\x02\n\tOperation\x12\x32\n\x04type\x18\x01 \x02(\x0e\x32$.biomaj.download.Operation.OPERATION\x12/\n\x08\x64ownload\x18\x02 \x01(\x0b\x32\x1d.biomaj.download.DownloadFile\x12)\n\x07process\x18\x03 \x01(\x0b\x32\x18.biomaj.download.Process\x12/\n\x05trace\x18\x04 \x01(\x0b\x32 .biomaj.download.Operation.Trace\x1a*\n\x05Trace\x12\x10\n\x08trace_id\x18\x01 \x02(\t\x12\x0f\n\x07span_id\x18\x02 \x02(\t\"0\n\tOPERATION\x12\x08\n\x04LIST\x10\x00\x12\x0c\n\x08\x44OWNLOAD\x10\x01\x12\x0b\n\x07PROCESS\x10\x02\"\x17\n\x07Process\x12\x0c\n\x04\x65xec\x18\x01 \x02(\t\"\x94\x0b\n\x0c\x44ownloadFile\x12\x0c\n\x04\x62\x61nk\x18\x01 \x02(\t\x12\x0f\n\x07session\x18\x02 \x02(\t\x12\x11\n\tlocal_dir\x18\x03 \x02(\t\x12\x18\n\x10timeout_download\x18\x04 \x01(\x05\x12=\n\x0bremote_file\x18\x05 \x02(\x0b\x32(.biomaj.download.DownloadFile.RemoteFile\x12\x32\n\x05proxy\x18\x06 \x01(\x0b\x32#.biomaj.download.DownloadFile.Proxy\x12\x43\n\x0bhttp_method\x18\x08 \x01(\x0e\x32).biomaj.download.DownloadFile.HTTP_METHOD:\x03GET\x12;\n\x07options\x18\t \x03(\x0b\x32*.biomaj.download.DownloadFile.OptionsEntry\x1a$\n\x05Param\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x1a\xcd\x03\n\tHttpParse\x12\x91\x01\n\x08\x64ir_line\x18\x01 \x02(\t:\x7f<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[DIR\\]\"[\\s]*/?>[\\s]*<a[\\s]+href=\"([\\S]+)/\"[\\s]*>.*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})\x12\xa5\x01\n\tfile_line\x18\x02 \x02(\t:\x91\x01<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[[\\s]+\\]\"[\\s]*/?>[\\s]<a[\\s]+href=\"([\\S]+)\".*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})[\\s]+([\\d\\.]+[MKG]{0,1})\x12\x13\n\x08\x64ir_name\x18\x03 \x02(\x05:\x01\x31\x12\x13\n\x08\x64ir_date\x18\x04 \x02(\x05:\x01\x32\x12\x14\n\tfile_name\x18\x05 \x02(\x05:\x01\x31\x12\x14\n\tfile_date\x18\x06 \x02(\x05:\x01\x32\x12\x18\n\x10\x66ile_date_format\x18\x07 \x01(\t\x12\x14\n\tfile_size\x18\x08 \x02(\x05:\x01\x33\x1a\xb8\x02\n\nRemoteFile\x12$\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x15.biomaj.download.File\x12\x38\n\x08protocol\x18\x02 \x02(\x0e\x32&.biomaj.download.DownloadFile.Protocol\x12\x0e\n\x06server\x18\x03 \x02(\t\x12\x12\n\nremote_dir\x18\x04 \x02(\t\x12\x0f\n\x07save_as\x18\x05 \x01(\t\x12\x32\n\x05param\x18\x06 \x03(\x0b\x32#.biomaj.download.DownloadFile.Param\x12;\n\nhttp_parse\x18\x07 \x01(\x0b\x32\'.biomaj.download.DownloadFile.HttpParse\x12\x13\n\x0b\x63redentials\x18\x08 \x01(\t\x12\x0f\n\x07matches\x18\t \x03(\t\x1a*\n\x05Proxy\x12\r\n\x05proxy\x18\x01 \x02(\t\x12\x12\n\nproxy_auth\x18\x02 \x01(\t\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x93\x01\n\x08Protocol\x12\x07\n\x03\x46TP\x10\x00\x12\x08\n\x04\x46TPS\x10\x01\x12\x08\n\x04HTTP\x10\x02\x12\t\n\x05HTTPS\x10\x03\x12\r\n\tDIRECTFTP\x10\x04\x12\x0e\n\nDIRECTHTTP\x10\x05\x12\x0f\n\x0b\x44IRECTHTTPS\x10\x06\x12\t\n\x05LOCAL\x10\x07\x12\t\n\x05RSYNC\x10\x08\x12\t\n\x05IRODS\x10\t\x12\x0e\n\nDIRECTFTPS\x10\n\" \n\x0bHTTP_METHOD\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'downmessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOWNLOADFILE_OPTIONSENTRY._options = None
  _DOWNLOADFILE_OPTIONSENTRY._serialized_options = b'8\001'
  _globals['_FILE']._serialized_start=39
  _globals['_FILE']._serialized_end=324
  _globals['_FILE_METADATA']._serialized_start=156
  _globals['_FILE_METADATA']._serialized_end=324
  _globals['_FILELIST']._serialized_start=326
  _globals['_FILELIST']._serialized_end=374
  _globals['_OPERATION']._serialized_start=377
  _globals['_OPERATION']._serialized_end=675
  _globals['_OPERATION_TRACE']._serialized_start=583
  _globals['_OPERATION_TRACE']._serialized_end=625
  _globals['_OPERATION_OPERATION']._serialized_start=627
  _globals['_OPERATION_OPERATION']._serialized_end=675
  _globals['_PROCESS']._serialized_start=677
  _globals['_PROCESS']._serialized_end=700
  _globals['_DOWNLOADFILE']._serialized_start=703
  _globals['_DOWNLOADFILE']._serialized_end=2131
  _globals['_DOWNLOADFILE_PARAM']._serialized_start=1040
  _globals['_DOWNLOADFILE_PARAM']._serialized_end=1076
  _globals['_DOWNLOADFILE_HTTPPARSE']._serialized_start=1079
  _globals['_DOWNLOADFILE_HTTPPARSE']._serialized_end=1540
  _globals['_DOWNLOADFILE_REMOTEFILE']._serialized_start=1543
  _globals['_DOWNLOADFILE_REMOTEFILE']._serialized_end=1855
  _globals['_DOWNLOADFILE_PROXY']._serialized_start=1857
  _globals['_DOWNLOADFILE_PROXY']._serialized_end=1899
  _globals['_DOWNLOADFILE_OPTIONSENTRY']._serialized_start=1901
  _globals['_DOWNLOADFILE_OPTIONSENTRY']._serialized_end=1947
  _globals['_DOWNLOADFILE_PROTOCOL']._serialized_start=1950
  _globals['_DOWNLOADFILE_PROTOCOL']._serialized_end=2097
  _globals['_DOWNLOADFILE_HTTP_METHOD']._serialized_start=2099
  _globals['_DOWNLOADFILE_HTTP_METHOD']._serialized_end=2131
# @@protoc_insertion_point(module_scope)
