# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import holoholo_shared_pb2 as holoholo__shared__pb2

from holoholo_shared_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='map.proto',
  package='PGo',
  syntax='proto3',
  serialized_pb=_b('\n\tmap.proto\x12\x03PGo\x1a\x15holoholo_shared.proto\"a\n\x11MapObjectsRequest\x12\x1f\n\x0c\x63\x65ll_request\x18\x01 \x01(\x0b\x32\t.PGo.Cell\x12\x10\n\x08unknown2\x18\x02 \x01(\x0c\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x0c\n\x04long\x18\x04 \x01(\x01\"+\n\x04\x43\x65ll\x12\x11\n\x05typea\x18\x80\x80\x80\xc0\x01 \x03(\x04\x12\x10\n\x05typeb\x18\x80\x80\x80@ \x03(\x04\".\n\x12MapObjectsResponse\x12\x18\n\x05tiles\x18\x01 \x03(\x0b\x32\t.PGo.Tile\"\x8e\x02\n\x04Tile\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x19\n\x11\x63urrent_timestamp\x18\x02 \x01(\x04\x12\x18\n\x05\x66orts\x18\x03 \x03(\x0b\x32\t.PGo.Fort\x12+\n\x0bspawn_start\x18\x05 \x03(\x0b\x32\x16.PGo.PokemonSpawnStart\x12\'\n\tspawn_end\x18\n \x03(\x0b\x32\x14.PGo.PokemonSpawnEnd\x12+\n\x0fpokemon_in_area\x18\x0b \x03(\x0b\x32\x12.PGo.PokemonInArea\x12 \n\tlocation9\x18\t \x03(\x0b\x32\r.PGo.Location\x12 \n\tlocation4\x18\x04 \x03(\x0b\x32\r.PGo.Location\"\xa7\x02\n\x04\x46ort\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x11\n\tnot_sure8\x18\x08 \x01(\x08\x12\x1c\n\x04team\x18\x05 \x01(\x0e\x32\x0e.PGo.TeamColor\x12\x18\n\x10guard_pokemon_id\x18\x06 \x01(\x04\x12\x10\n\x08prestige\x18\n \x01(\x04\x12\x14\n\x0cis_in_battle\x18\x0b \x01(\x08\x12\x13\n\x0bis_pokestop\x18\t \x01(\x08\x12\x10\n\x08reset_ts\x18\x0e \x01(\x04\x12\x16\n\x0e\x61\x63tive_lure_id\x18\x0c \x01(\x0c\x12)\n\x0e\x66ort_lure_info\x18\r \x01(\x0b\x32\x11.PGo.FortLureInfo\"h\n\x0c\x46ortLureInfo\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x11\n\tnot_sure2\x18\x02 \x01(\x01\x12!\n\x07pokemon\x18\x03 \x01(\x0e\x32\x10.PGo.PokemonName\x12\x11\n\texpiry_ts\x18\x04 \x01(\x04\"\xf0\x01\n\x11PokemonSpawnStart\x12\x0b\n\x03uid\x18\x01 \x01(\x01\x12\x13\n\x0b\x61ppeared_ts\x18\x02 \x01(\x04\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x14\n\x0cs2cell_token\x18\x05 \x01(\t\x12\x38\n\x0cpokemon_info\x18\x07 \x01(\x0b\x32\".PGo.PokemonSpawnStart.PokemonInfo\x12\x12\n\nnot_sure11\x18\x0b \x01(\x05\x1a\x30\n\x0bPokemonInfo\x12!\n\x07pokemon\x18\x02 \x01(\x0e\x32\x10.PGo.PokemonName\"\x8f\x01\n\x0fPokemonSpawnEnd\x12\x14\n\x0cs2cell_token\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\x01\x12!\n\x07pokemon\x18\x03 \x01(\x0e\x32\x10.PGo.PokemonName\x12\x11\n\texpiry_ts\x18\x04 \x01(\x04\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01\"Q\n\rPokemonInArea\x12!\n\x07pokemon\x18\x01 \x01(\x0e\x32\x10.PGo.PokemonName\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x12\x0b\n\x03uid\x18\x03 \x01(\x01\"/\n\x08Location\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01P\x00\x62\x06proto3')
  ,
  dependencies=[holoholo__shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAPOBJECTSREQUEST = _descriptor.Descriptor(
  name='MapObjectsRequest',
  full_name='PGo.MapObjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_request', full_name='PGo.MapObjectsRequest.cell_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='PGo.MapObjectsRequest.unknown2', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='PGo.MapObjectsRequest.lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='PGo.MapObjectsRequest.long', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  serialized_start=41,
  serialized_end=138,
)


_CELL = _descriptor.Descriptor(
  name='Cell',
  full_name='PGo.Cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='typea', full_name='PGo.Cell.typea', index=0,
      number=402653184, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='typeb', full_name='PGo.Cell.typeb', index=1,
      number=134217728, type=4, cpp_type=4, label=3,
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
  serialized_start=140,
  serialized_end=183,
)


_MAPOBJECTSRESPONSE = _descriptor.Descriptor(
  name='MapObjectsResponse',
  full_name='PGo.MapObjectsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tiles', full_name='PGo.MapObjectsResponse.tiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=185,
  serialized_end=231,
)


_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='PGo.Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.Tile.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_timestamp', full_name='PGo.Tile.current_timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forts', full_name='PGo.Tile.forts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_start', full_name='PGo.Tile.spawn_start', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_end', full_name='PGo.Tile.spawn_end', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_in_area', full_name='PGo.Tile.pokemon_in_area', index=5,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location9', full_name='PGo.Tile.location9', index=6,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location4', full_name='PGo.Tile.location4', index=7,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=234,
  serialized_end=504,
)


_FORT = _descriptor.Descriptor(
  name='Fort',
  full_name='PGo.Fort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PGo.Fort.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PGo.Fort.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PGo.Fort.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PGo.Fort.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='not_sure8', full_name='PGo.Fort.not_sure8', index=4,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='PGo.Fort.team', index=5,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guard_pokemon_id', full_name='PGo.Fort.guard_pokemon_id', index=6,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige', full_name='PGo.Fort.prestige', index=7,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_in_battle', full_name='PGo.Fort.is_in_battle', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_pokestop', full_name='PGo.Fort.is_pokestop', index=9,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_ts', full_name='PGo.Fort.reset_ts', index=10,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_lure_id', full_name='PGo.Fort.active_lure_id', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_lure_info', full_name='PGo.Fort.fort_lure_info', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=507,
  serialized_end=802,
)


_FORTLUREINFO = _descriptor.Descriptor(
  name='FortLureInfo',
  full_name='PGo.FortLureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='PGo.FortLureInfo.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='not_sure2', full_name='PGo.FortLureInfo.not_sure2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='PGo.FortLureInfo.pokemon', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiry_ts', full_name='PGo.FortLureInfo.expiry_ts', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=804,
  serialized_end=908,
)


_POKEMONSPAWNSTART_POKEMONINFO = _descriptor.Descriptor(
  name='PokemonInfo',
  full_name='PGo.PokemonSpawnStart.PokemonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='PGo.PokemonSpawnStart.PokemonInfo.pokemon', index=0,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=1103,
  serialized_end=1151,
)

_POKEMONSPAWNSTART = _descriptor.Descriptor(
  name='PokemonSpawnStart',
  full_name='PGo.PokemonSpawnStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='PGo.PokemonSpawnStart.uid', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appeared_ts', full_name='PGo.PokemonSpawnStart.appeared_ts', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PGo.PokemonSpawnStart.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PGo.PokemonSpawnStart.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s2cell_token', full_name='PGo.PokemonSpawnStart.s2cell_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_info', full_name='PGo.PokemonSpawnStart.pokemon_info', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='not_sure11', full_name='PGo.PokemonSpawnStart.not_sure11', index=6,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_POKEMONSPAWNSTART_POKEMONINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=911,
  serialized_end=1151,
)


_POKEMONSPAWNEND = _descriptor.Descriptor(
  name='PokemonSpawnEnd',
  full_name='PGo.PokemonSpawnEnd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s2cell_token', full_name='PGo.PokemonSpawnEnd.s2cell_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='PGo.PokemonSpawnEnd.uid', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='PGo.PokemonSpawnEnd.pokemon', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiry_ts', full_name='PGo.PokemonSpawnEnd.expiry_ts', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PGo.PokemonSpawnEnd.latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PGo.PokemonSpawnEnd.longitude', index=5,
      number=6, type=1, cpp_type=5, label=1,
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
  serialized_start=1154,
  serialized_end=1297,
)


_POKEMONINAREA = _descriptor.Descriptor(
  name='PokemonInArea',
  full_name='PGo.PokemonInArea',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='PGo.PokemonInArea.pokemon', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='PGo.PokemonInArea.distance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='PGo.PokemonInArea.uid', index=2,
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
  serialized_start=1299,
  serialized_end=1380,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='PGo.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PGo.Location.latitude', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PGo.Location.longitude', index=1,
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
  serialized_start=1382,
  serialized_end=1429,
)

_MAPOBJECTSREQUEST.fields_by_name['cell_request'].message_type = _CELL
_MAPOBJECTSRESPONSE.fields_by_name['tiles'].message_type = _TILE
_TILE.fields_by_name['forts'].message_type = _FORT
_TILE.fields_by_name['spawn_start'].message_type = _POKEMONSPAWNSTART
_TILE.fields_by_name['spawn_end'].message_type = _POKEMONSPAWNEND
_TILE.fields_by_name['pokemon_in_area'].message_type = _POKEMONINAREA
_TILE.fields_by_name['location9'].message_type = _LOCATION
_TILE.fields_by_name['location4'].message_type = _LOCATION
_FORT.fields_by_name['team'].enum_type = holoholo__shared__pb2._TEAMCOLOR
_FORT.fields_by_name['fort_lure_info'].message_type = _FORTLUREINFO
_FORTLUREINFO.fields_by_name['pokemon'].enum_type = holoholo__shared__pb2._POKEMONNAME
_POKEMONSPAWNSTART_POKEMONINFO.fields_by_name['pokemon'].enum_type = holoholo__shared__pb2._POKEMONNAME
_POKEMONSPAWNSTART_POKEMONINFO.containing_type = _POKEMONSPAWNSTART
_POKEMONSPAWNSTART.fields_by_name['pokemon_info'].message_type = _POKEMONSPAWNSTART_POKEMONINFO
_POKEMONSPAWNEND.fields_by_name['pokemon'].enum_type = holoholo__shared__pb2._POKEMONNAME
_POKEMONINAREA.fields_by_name['pokemon'].enum_type = holoholo__shared__pb2._POKEMONNAME
DESCRIPTOR.message_types_by_name['MapObjectsRequest'] = _MAPOBJECTSREQUEST
DESCRIPTOR.message_types_by_name['Cell'] = _CELL
DESCRIPTOR.message_types_by_name['MapObjectsResponse'] = _MAPOBJECTSRESPONSE
DESCRIPTOR.message_types_by_name['Tile'] = _TILE
DESCRIPTOR.message_types_by_name['Fort'] = _FORT
DESCRIPTOR.message_types_by_name['FortLureInfo'] = _FORTLUREINFO
DESCRIPTOR.message_types_by_name['PokemonSpawnStart'] = _POKEMONSPAWNSTART
DESCRIPTOR.message_types_by_name['PokemonSpawnEnd'] = _POKEMONSPAWNEND
DESCRIPTOR.message_types_by_name['PokemonInArea'] = _POKEMONINAREA
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION

MapObjectsRequest = _reflection.GeneratedProtocolMessageType('MapObjectsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MAPOBJECTSREQUEST,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.MapObjectsRequest)
  ))
_sym_db.RegisterMessage(MapObjectsRequest)

Cell = _reflection.GeneratedProtocolMessageType('Cell', (_message.Message,), dict(
  DESCRIPTOR = _CELL,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.Cell)
  ))
_sym_db.RegisterMessage(Cell)

MapObjectsResponse = _reflection.GeneratedProtocolMessageType('MapObjectsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MAPOBJECTSRESPONSE,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.MapObjectsResponse)
  ))
_sym_db.RegisterMessage(MapObjectsResponse)

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), dict(
  DESCRIPTOR = _TILE,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.Tile)
  ))
_sym_db.RegisterMessage(Tile)

Fort = _reflection.GeneratedProtocolMessageType('Fort', (_message.Message,), dict(
  DESCRIPTOR = _FORT,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.Fort)
  ))
_sym_db.RegisterMessage(Fort)

FortLureInfo = _reflection.GeneratedProtocolMessageType('FortLureInfo', (_message.Message,), dict(
  DESCRIPTOR = _FORTLUREINFO,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortLureInfo)
  ))
_sym_db.RegisterMessage(FortLureInfo)

PokemonSpawnStart = _reflection.GeneratedProtocolMessageType('PokemonSpawnStart', (_message.Message,), dict(

  PokemonInfo = _reflection.GeneratedProtocolMessageType('PokemonInfo', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONSPAWNSTART_POKEMONINFO,
    __module__ = 'map_pb2'
    # @@protoc_insertion_point(class_scope:PGo.PokemonSpawnStart.PokemonInfo)
    ))
  ,
  DESCRIPTOR = _POKEMONSPAWNSTART,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PokemonSpawnStart)
  ))
_sym_db.RegisterMessage(PokemonSpawnStart)
_sym_db.RegisterMessage(PokemonSpawnStart.PokemonInfo)

PokemonSpawnEnd = _reflection.GeneratedProtocolMessageType('PokemonSpawnEnd', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONSPAWNEND,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PokemonSpawnEnd)
  ))
_sym_db.RegisterMessage(PokemonSpawnEnd)

PokemonInArea = _reflection.GeneratedProtocolMessageType('PokemonInArea', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONINAREA,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PokemonInArea)
  ))
_sym_db.RegisterMessage(PokemonInArea)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'map_pb2'
  # @@protoc_insertion_point(class_scope:PGo.Location)
  ))
_sym_db.RegisterMessage(Location)


# @@protoc_insertion_point(module_scope)
