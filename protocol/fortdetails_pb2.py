# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fortdetails.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fortdetails.proto',
  package='PGo',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x66ortdetails.proto\x12\x03PGo\"\xf3\x01\n\x13\x46ortDetailsOutProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\x12\n\nisPokeStop\x18\t \x01(\x08\x12\x0b\n\x03lat\x18\n \x01(\x01\x12\x0c\n\x04long\x18\x0b \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12+\n\x04lure\x18\r \x01(\x0b\x32\x1d.PGo.FortDetailsOutProto.Lure\x1a>\n\x04Lure\x12\x11\n\tsomething\x18\x01 \x01(\r\x12\x12\n\nexpiration\x18\x02 \x01(\x04\x12\x0f\n\x07trainer\x18\x03 \x01(\t\"9\n\x10\x46ortDetailsProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03lat\x18\x02 \x01(\x01\x12\x0c\n\x04long\x18\x03 \x01(\x01\"U\n\x0f\x46ortSearchProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03lat\x18\x02 \x01(\x01\x12\x0c\n\x04long\x18\x03 \x01(\x01\x12\x0c\n\x04lat2\x18\x04 \x01(\x01\x12\r\n\x05long2\x18\x05 \x01(\x01\"\x93\x01\n\x12\x46ortSearchOutProto\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12.\n\x06result\x18\x02 \x01(\x0b\x32\x1e.PGo.FortSearchOutProto.Result\x1a<\n\x06Result\x12\x0b\n\x03ts1\x18\x01 \x01(\x04\x12\x0b\n\x03ts2\x18\x02 \x01(\x04\x12\x18\n\x05items\x18\x03 \x03(\x0b\x32\t.PGo.Item\"\x19\n\x04Item\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\"\xaf\x04\n\x03Gym\x12!\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x10.PGo.Gym.Details\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\timage_url\x18\x03 \x01(\t\x12\x0c\n\x04team\x18\x04 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x1a\xc0\x03\n\x07\x44\x65tails\x12-\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x1c.PGo.Gym.Details.MoreDetails\x12&\n\x06levels\x18\x02 \x03(\x0b\x32\x16.PGo.Gym.Details.Level\x1aY\n\x0bMoreDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x0c\n\x04long\x18\x04 \x01(\x01\x12\x10\n\x08prestige\x18\n \x01(\x04\x1a\x82\x02\n\x05Level\x12/\n\x07pokemon\x18\x01 \x01(\x0b\x32\x1e.PGo.Gym.Details.Level.Pokemon\x12/\n\x07trainer\x18\x02 \x01(\x0b\x32\x1e.PGo.Gym.Details.Level.Trainer\x1ao\n\x07Pokemon\x12\n\n\x02\x63p\x18\x03 \x01(\x04\x12\x15\n\rcurrentHealth\x18\x04 \x01(\x04\x12\x11\n\tmaxHealth\x18\x05 \x01(\x04\x12\x0f\n\x07trainer\x18\t \x01(\t\x12\n\n\x02id\x18\x16 \x01(\x04\x12\x11\n\ttimestmap\x18\x1a \x01(\x04\x1a&\n\x07Trainer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTDETAILSOUTPROTO_LURE = _descriptor.Descriptor(
  name='Lure',
  full_name='PGo.FortDetailsOutProto.Lure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='something', full_name='PGo.FortDetailsOutProto.Lure.something', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='PGo.FortDetailsOutProto.Lure.expiration', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer', full_name='PGo.FortDetailsOutProto.Lure.trainer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=270,
)

_FORTDETAILSOUTPROTO = _descriptor.Descriptor(
  name='FortDetailsOutProto',
  full_name='PGo.FortDetailsOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.FortDetailsOutProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='PGo.FortDetailsOutProto.name', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='PGo.FortDetailsOutProto.image_url', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isPokeStop', full_name='PGo.FortDetailsOutProto.isPokeStop', index=3,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='PGo.FortDetailsOutProto.lat', index=4,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='PGo.FortDetailsOutProto.long', index=5,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='PGo.FortDetailsOutProto.description', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lure', full_name='PGo.FortDetailsOutProto.lure', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FORTDETAILSOUTPROTO_LURE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=270,
)


_FORTDETAILSPROTO = _descriptor.Descriptor(
  name='FortDetailsProto',
  full_name='PGo.FortDetailsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.FortDetailsProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='PGo.FortDetailsProto.lat', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='PGo.FortDetailsProto.long', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=329,
)


_FORTSEARCHPROTO = _descriptor.Descriptor(
  name='FortSearchProto',
  full_name='PGo.FortSearchProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.FortSearchProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='PGo.FortSearchProto.lat', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='PGo.FortSearchProto.long', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat2', full_name='PGo.FortSearchProto.lat2', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long2', full_name='PGo.FortSearchProto.long2', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=416,
)


_FORTSEARCHOUTPROTO_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='PGo.FortSearchOutProto.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts1', full_name='PGo.FortSearchOutProto.Result.ts1', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts2', full_name='PGo.FortSearchOutProto.Result.ts2', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='PGo.FortSearchOutProto.Result.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=566,
)

_FORTSEARCHOUTPROTO = _descriptor.Descriptor(
  name='FortSearchOutProto',
  full_name='PGo.FortSearchOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='PGo.FortSearchOutProto.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='PGo.FortSearchOutProto.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FORTSEARCHOUTPROTO_RESULT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=419,
  serialized_end=566,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='PGo.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PGo.Item.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=593,
)


_GYM_DETAILS_MOREDETAILS = _descriptor.Descriptor(
  name='MoreDetails',
  full_name='PGo.Gym.Details.MoreDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.Gym.Details.MoreDetails.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PGo.Gym.Details.MoreDetails.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='PGo.Gym.Details.MoreDetails.lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='PGo.Gym.Details.MoreDetails.long', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige', full_name='PGo.Gym.Details.MoreDetails.prestige', index=4,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=894,
)

_GYM_DETAILS_LEVEL_POKEMON = _descriptor.Descriptor(
  name='Pokemon',
  full_name='PGo.Gym.Details.Level.Pokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cp', full_name='PGo.Gym.Details.Level.Pokemon.cp', index=0,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currentHealth', full_name='PGo.Gym.Details.Level.Pokemon.currentHealth', index=1,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxHealth', full_name='PGo.Gym.Details.Level.Pokemon.maxHealth', index=2,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer', full_name='PGo.Gym.Details.Level.Pokemon.trainer', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.Gym.Details.Level.Pokemon.id', index=4,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestmap', full_name='PGo.Gym.Details.Level.Pokemon.timestmap', index=5,
      number=26, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1004,
  serialized_end=1115,
)

_GYM_DETAILS_LEVEL_TRAINER = _descriptor.Descriptor(
  name='Trainer',
  full_name='PGo.Gym.Details.Level.Trainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PGo.Gym.Details.Level.Trainer.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='PGo.Gym.Details.Level.Trainer.level', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1117,
  serialized_end=1155,
)

_GYM_DETAILS_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='PGo.Gym.Details.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='PGo.Gym.Details.Level.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer', full_name='PGo.Gym.Details.Level.trainer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GYM_DETAILS_LEVEL_POKEMON, _GYM_DETAILS_LEVEL_TRAINER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=897,
  serialized_end=1155,
)

_GYM_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='PGo.Gym.Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='PGo.Gym.Details.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='levels', full_name='PGo.Gym.Details.levels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GYM_DETAILS_MOREDETAILS, _GYM_DETAILS_LEVEL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=707,
  serialized_end=1155,
)

_GYM = _descriptor.Descriptor(
  name='Gym',
  full_name='PGo.Gym',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='PGo.Gym.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='PGo.Gym.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='PGo.Gym.image_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='PGo.Gym.team', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='PGo.Gym.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GYM_DETAILS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=596,
  serialized_end=1155,
)

_FORTDETAILSOUTPROTO_LURE.containing_type = _FORTDETAILSOUTPROTO
_FORTDETAILSOUTPROTO.fields_by_name['lure'].message_type = _FORTDETAILSOUTPROTO_LURE
_FORTSEARCHOUTPROTO_RESULT.fields_by_name['items'].message_type = _ITEM
_FORTSEARCHOUTPROTO_RESULT.containing_type = _FORTSEARCHOUTPROTO
_FORTSEARCHOUTPROTO.fields_by_name['result'].message_type = _FORTSEARCHOUTPROTO_RESULT
_GYM_DETAILS_MOREDETAILS.containing_type = _GYM_DETAILS
_GYM_DETAILS_LEVEL_POKEMON.containing_type = _GYM_DETAILS_LEVEL
_GYM_DETAILS_LEVEL_TRAINER.containing_type = _GYM_DETAILS_LEVEL
_GYM_DETAILS_LEVEL.fields_by_name['pokemon'].message_type = _GYM_DETAILS_LEVEL_POKEMON
_GYM_DETAILS_LEVEL.fields_by_name['trainer'].message_type = _GYM_DETAILS_LEVEL_TRAINER
_GYM_DETAILS_LEVEL.containing_type = _GYM_DETAILS
_GYM_DETAILS.fields_by_name['details'].message_type = _GYM_DETAILS_MOREDETAILS
_GYM_DETAILS.fields_by_name['levels'].message_type = _GYM_DETAILS_LEVEL
_GYM_DETAILS.containing_type = _GYM
_GYM.fields_by_name['details'].message_type = _GYM_DETAILS
DESCRIPTOR.message_types_by_name['FortDetailsOutProto'] = _FORTDETAILSOUTPROTO
DESCRIPTOR.message_types_by_name['FortDetailsProto'] = _FORTDETAILSPROTO
DESCRIPTOR.message_types_by_name['FortSearchProto'] = _FORTSEARCHPROTO
DESCRIPTOR.message_types_by_name['FortSearchOutProto'] = _FORTSEARCHOUTPROTO
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Gym'] = _GYM

FortDetailsOutProto = _reflection.GeneratedProtocolMessageType('FortDetailsOutProto', (_message.Message,), dict(

  Lure = _reflection.GeneratedProtocolMessageType('Lure', (_message.Message,), dict(
    DESCRIPTOR = _FORTDETAILSOUTPROTO_LURE,
    __module__ = 'fortdetails_pb2'
    # @@protoc_insertion_point(class_scope:PGo.FortDetailsOutProto.Lure)
    ))
  ,
  DESCRIPTOR = _FORTDETAILSOUTPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortDetailsOutProto)
  ))
_sym_db.RegisterMessage(FortDetailsOutProto)
_sym_db.RegisterMessage(FortDetailsOutProto.Lure)

FortDetailsProto = _reflection.GeneratedProtocolMessageType('FortDetailsProto', (_message.Message,), dict(
  DESCRIPTOR = _FORTDETAILSPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortDetailsProto)
  ))
_sym_db.RegisterMessage(FortDetailsProto)

FortSearchProto = _reflection.GeneratedProtocolMessageType('FortSearchProto', (_message.Message,), dict(
  DESCRIPTOR = _FORTSEARCHPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortSearchProto)
  ))
_sym_db.RegisterMessage(FortSearchProto)

FortSearchOutProto = _reflection.GeneratedProtocolMessageType('FortSearchOutProto', (_message.Message,), dict(

  Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
    DESCRIPTOR = _FORTSEARCHOUTPROTO_RESULT,
    __module__ = 'fortdetails_pb2'
    # @@protoc_insertion_point(class_scope:PGo.FortSearchOutProto.Result)
    ))
  ,
  DESCRIPTOR = _FORTSEARCHOUTPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortSearchOutProto)
  ))
_sym_db.RegisterMessage(FortSearchOutProto)
_sym_db.RegisterMessage(FortSearchOutProto.Result)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.Item)
  ))
_sym_db.RegisterMessage(Item)

Gym = _reflection.GeneratedProtocolMessageType('Gym', (_message.Message,), dict(

  Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), dict(

    MoreDetails = _reflection.GeneratedProtocolMessageType('MoreDetails', (_message.Message,), dict(
      DESCRIPTOR = _GYM_DETAILS_MOREDETAILS,
      __module__ = 'fortdetails_pb2'
      # @@protoc_insertion_point(class_scope:PGo.Gym.Details.MoreDetails)
      ))
    ,

    Level = _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), dict(

      Pokemon = _reflection.GeneratedProtocolMessageType('Pokemon', (_message.Message,), dict(
        DESCRIPTOR = _GYM_DETAILS_LEVEL_POKEMON,
        __module__ = 'fortdetails_pb2'
        # @@protoc_insertion_point(class_scope:PGo.Gym.Details.Level.Pokemon)
        ))
      ,

      Trainer = _reflection.GeneratedProtocolMessageType('Trainer', (_message.Message,), dict(
        DESCRIPTOR = _GYM_DETAILS_LEVEL_TRAINER,
        __module__ = 'fortdetails_pb2'
        # @@protoc_insertion_point(class_scope:PGo.Gym.Details.Level.Trainer)
        ))
      ,
      DESCRIPTOR = _GYM_DETAILS_LEVEL,
      __module__ = 'fortdetails_pb2'
      # @@protoc_insertion_point(class_scope:PGo.Gym.Details.Level)
      ))
    ,
    DESCRIPTOR = _GYM_DETAILS,
    __module__ = 'fortdetails_pb2'
    # @@protoc_insertion_point(class_scope:PGo.Gym.Details)
    ))
  ,
  DESCRIPTOR = _GYM,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.Gym)
  ))
_sym_db.RegisterMessage(Gym)
_sym_db.RegisterMessage(Gym.Details)
_sym_db.RegisterMessage(Gym.Details.MoreDetails)
_sym_db.RegisterMessage(Gym.Details.Level)
_sym_db.RegisterMessage(Gym.Details.Level.Pokemon)
_sym_db.RegisterMessage(Gym.Details.Level.Trainer)


# @@protoc_insertion_point(module_scope)
