# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recipe_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='recipe_service.proto',
  package='recipe',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14recipe_service.proto\x12\x06recipe\"\x1e\n\x10GetRecipeRequest\x12\n\n\x02id\x18\x01 \x01(\t\"3\n\x11GetRecipeResponse\x12\x1e\n\x06recipe\x18\x01 \x01(\x0b\x32\x0e.recipe.Recipe\"5\n\x13\x43reateRecipeRequest\x12\x1e\n\x06recipe\x18\x01 \x01(\x0b\x32\x0e.recipe.Recipe\"\x16\n\x14\x43reateRecipeResponse\"T\n\x06Recipe\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1b\n\x05steps\x18\n \x03(\x0b\x32\x0c.recipe.Step\"\x80\x02\n\x04Step\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\trecipe_id\x18\x02 \x01(\t\x12\x19\n\x11previous_step_ids\x18\x03 \x03(\t\x12#\n\x04type\x18\x04 \x01(\x0e\x32\x15.recipe.Step.StepType\x12\x31\n\x0fget_ingredients\x18\n \x01(\x0b\x32\x16.recipe.GetIngredientsH\x00\x12!\n\x07\x63ook_it\x18\x0b \x01(\x0b\x32\x0e.recipe.CookItH\x00\"9\n\x08StepType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fGET_INGREDIENTS\x10\x01\x12\x0b\n\x07\x43OOK_IT\x10\x02\x42\x08\n\x06\x64\x65tail\"f\n\x0eGetIngredients\x12=\n\x10ingredients_type\x18\x01 \x01(\x0e\x32#.recipe.Ingredients.IngredientsType\x12\x15\n\rserving_count\x18\x02 \x01(\x01\"\x90\x02\n\x0bIngredients\x12=\n\x10ingredients_type\x18\x01 \x01(\x0e\x32#.recipe.Ingredients.IngredientsType\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x03\x12\x0f\n\x07\x63\x61lorie\x18\x04 \x01(\x03\x12\x12\n\x08kilogram\x18\x14 \x01(\x03H\x00\x12\x14\n\nmilliliter\x18\x15 \x01(\x03H\x00\x12\x14\n\x0cpicture_urls\x18\n \x03(\t\"=\n\x0fIngredientsType\x12\x17\n\x13UNKNOWN_INGREDIENTS\x10\x00\x12\x08\n\x04RICE\x10\x01\x12\x07\n\x03OIL\x10\x02\x42\x0e\n\x0cserving_base\"V\n\x06\x43ookIt\x12;\n\x10\x63ook_method_type\x18\x01 \x01(\x0e\x32!.recipe.CookMethod.CookMethodType\x12\x0f\n\x07seconds\x18\x02 \x01(\x03\"\xa7\x01\n\nCookMethod\x12;\n\x10\x63ook_method_type\x18\x01 \x01(\x0e\x32!.recipe.CookMethod.CookMethodType\x12\x12\n\nis_waiting\x18\x02 \x01(\x08\"H\n\x0e\x43ookMethodType\x12\x17\n\x13UNKNOWN_COOK_METHOD\x10\x00\x12\t\n\x05STEAM\x10\x01\x12\x07\n\x03\x46RY\x10\x02\x12\t\n\x05ROAST\x10\x03\x32\xa0\x01\n\rRecipeService\x12\x42\n\tGetRecipe\x12\x18.recipe.GetRecipeRequest\x1a\x19.recipe.GetRecipeResponse\"\x00\x12K\n\x0c\x43reateRecipe\x12\x1b.recipe.CreateRecipeRequest\x1a\x1c.recipe.CreateRecipeResponse\"\x00\x62\x06proto3')
)



_STEP_STEPTYPE = _descriptor.EnumDescriptor(
  name='StepType',
  full_name='recipe.Step.StepType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INGREDIENTS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOK_IT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=472,
  serialized_end=529,
)
_sym_db.RegisterEnumDescriptor(_STEP_STEPTYPE)

_INGREDIENTS_INGREDIENTSTYPE = _descriptor.EnumDescriptor(
  name='IngredientsType',
  full_name='recipe.Ingredients.IngredientsType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_INGREDIENTS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RICE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OIL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=841,
  serialized_end=902,
)
_sym_db.RegisterEnumDescriptor(_INGREDIENTS_INGREDIENTSTYPE)

_COOKMETHOD_COOKMETHODTYPE = _descriptor.EnumDescriptor(
  name='CookMethodType',
  full_name='recipe.CookMethod.CookMethodType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_COOK_METHOD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEAM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROAST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1104,
  serialized_end=1176,
)
_sym_db.RegisterEnumDescriptor(_COOKMETHOD_COOKMETHODTYPE)


_GETRECIPEREQUEST = _descriptor.Descriptor(
  name='GetRecipeRequest',
  full_name='recipe.GetRecipeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='recipe.GetRecipeRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=62,
)


_GETRECIPERESPONSE = _descriptor.Descriptor(
  name='GetRecipeResponse',
  full_name='recipe.GetRecipeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipe', full_name='recipe.GetRecipeResponse.recipe', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=115,
)


_CREATERECIPEREQUEST = _descriptor.Descriptor(
  name='CreateRecipeRequest',
  full_name='recipe.CreateRecipeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipe', full_name='recipe.CreateRecipeRequest.recipe', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=170,
)


_CREATERECIPERESPONSE = _descriptor.Descriptor(
  name='CreateRecipeResponse',
  full_name='recipe.CreateRecipeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=194,
)


_RECIPE = _descriptor.Descriptor(
  name='Recipe',
  full_name='recipe.Recipe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='recipe.Recipe.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='recipe.Recipe.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='recipe.Recipe.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='recipe.Recipe.steps', index=3,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=280,
)


_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='recipe.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='recipe.Step.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipe_id', full_name='recipe.Step.recipe_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_step_ids', full_name='recipe.Step.previous_step_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='recipe.Step.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_ingredients', full_name='recipe.Step.get_ingredients', index=4,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cook_it', full_name='recipe.Step.cook_it', index=5,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STEP_STEPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='detail', full_name='recipe.Step.detail',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=283,
  serialized_end=539,
)


_GETINGREDIENTS = _descriptor.Descriptor(
  name='GetIngredients',
  full_name='recipe.GetIngredients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingredients_type', full_name='recipe.GetIngredients.ingredients_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serving_count', full_name='recipe.GetIngredients.serving_count', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=643,
)


_INGREDIENTS = _descriptor.Descriptor(
  name='Ingredients',
  full_name='recipe.Ingredients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingredients_type', full_name='recipe.Ingredients.ingredients_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='recipe.Ingredients.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='recipe.Ingredients.price', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calorie', full_name='recipe.Ingredients.calorie', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kilogram', full_name='recipe.Ingredients.kilogram', index=4,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milliliter', full_name='recipe.Ingredients.milliliter', index=5,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='picture_urls', full_name='recipe.Ingredients.picture_urls', index=6,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INGREDIENTS_INGREDIENTSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='serving_base', full_name='recipe.Ingredients.serving_base',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=646,
  serialized_end=918,
)


_COOKIT = _descriptor.Descriptor(
  name='CookIt',
  full_name='recipe.CookIt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cook_method_type', full_name='recipe.CookIt.cook_method_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='recipe.CookIt.seconds', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=920,
  serialized_end=1006,
)


_COOKMETHOD = _descriptor.Descriptor(
  name='CookMethod',
  full_name='recipe.CookMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cook_method_type', full_name='recipe.CookMethod.cook_method_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_waiting', full_name='recipe.CookMethod.is_waiting', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COOKMETHOD_COOKMETHODTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1009,
  serialized_end=1176,
)

_GETRECIPERESPONSE.fields_by_name['recipe'].message_type = _RECIPE
_CREATERECIPEREQUEST.fields_by_name['recipe'].message_type = _RECIPE
_RECIPE.fields_by_name['steps'].message_type = _STEP
_STEP.fields_by_name['type'].enum_type = _STEP_STEPTYPE
_STEP.fields_by_name['get_ingredients'].message_type = _GETINGREDIENTS
_STEP.fields_by_name['cook_it'].message_type = _COOKIT
_STEP_STEPTYPE.containing_type = _STEP
_STEP.oneofs_by_name['detail'].fields.append(
  _STEP.fields_by_name['get_ingredients'])
_STEP.fields_by_name['get_ingredients'].containing_oneof = _STEP.oneofs_by_name['detail']
_STEP.oneofs_by_name['detail'].fields.append(
  _STEP.fields_by_name['cook_it'])
_STEP.fields_by_name['cook_it'].containing_oneof = _STEP.oneofs_by_name['detail']
_GETINGREDIENTS.fields_by_name['ingredients_type'].enum_type = _INGREDIENTS_INGREDIENTSTYPE
_INGREDIENTS.fields_by_name['ingredients_type'].enum_type = _INGREDIENTS_INGREDIENTSTYPE
_INGREDIENTS_INGREDIENTSTYPE.containing_type = _INGREDIENTS
_INGREDIENTS.oneofs_by_name['serving_base'].fields.append(
  _INGREDIENTS.fields_by_name['kilogram'])
_INGREDIENTS.fields_by_name['kilogram'].containing_oneof = _INGREDIENTS.oneofs_by_name['serving_base']
_INGREDIENTS.oneofs_by_name['serving_base'].fields.append(
  _INGREDIENTS.fields_by_name['milliliter'])
_INGREDIENTS.fields_by_name['milliliter'].containing_oneof = _INGREDIENTS.oneofs_by_name['serving_base']
_COOKIT.fields_by_name['cook_method_type'].enum_type = _COOKMETHOD_COOKMETHODTYPE
_COOKMETHOD.fields_by_name['cook_method_type'].enum_type = _COOKMETHOD_COOKMETHODTYPE
_COOKMETHOD_COOKMETHODTYPE.containing_type = _COOKMETHOD
DESCRIPTOR.message_types_by_name['GetRecipeRequest'] = _GETRECIPEREQUEST
DESCRIPTOR.message_types_by_name['GetRecipeResponse'] = _GETRECIPERESPONSE
DESCRIPTOR.message_types_by_name['CreateRecipeRequest'] = _CREATERECIPEREQUEST
DESCRIPTOR.message_types_by_name['CreateRecipeResponse'] = _CREATERECIPERESPONSE
DESCRIPTOR.message_types_by_name['Recipe'] = _RECIPE
DESCRIPTOR.message_types_by_name['Step'] = _STEP
DESCRIPTOR.message_types_by_name['GetIngredients'] = _GETINGREDIENTS
DESCRIPTOR.message_types_by_name['Ingredients'] = _INGREDIENTS
DESCRIPTOR.message_types_by_name['CookIt'] = _COOKIT
DESCRIPTOR.message_types_by_name['CookMethod'] = _COOKMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRecipeRequest = _reflection.GeneratedProtocolMessageType('GetRecipeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRECIPEREQUEST,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.GetRecipeRequest)
  ))
_sym_db.RegisterMessage(GetRecipeRequest)

GetRecipeResponse = _reflection.GeneratedProtocolMessageType('GetRecipeResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRECIPERESPONSE,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.GetRecipeResponse)
  ))
_sym_db.RegisterMessage(GetRecipeResponse)

CreateRecipeRequest = _reflection.GeneratedProtocolMessageType('CreateRecipeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATERECIPEREQUEST,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.CreateRecipeRequest)
  ))
_sym_db.RegisterMessage(CreateRecipeRequest)

CreateRecipeResponse = _reflection.GeneratedProtocolMessageType('CreateRecipeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATERECIPERESPONSE,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.CreateRecipeResponse)
  ))
_sym_db.RegisterMessage(CreateRecipeResponse)

Recipe = _reflection.GeneratedProtocolMessageType('Recipe', (_message.Message,), dict(
  DESCRIPTOR = _RECIPE,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.Recipe)
  ))
_sym_db.RegisterMessage(Recipe)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), dict(
  DESCRIPTOR = _STEP,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.Step)
  ))
_sym_db.RegisterMessage(Step)

GetIngredients = _reflection.GeneratedProtocolMessageType('GetIngredients', (_message.Message,), dict(
  DESCRIPTOR = _GETINGREDIENTS,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.GetIngredients)
  ))
_sym_db.RegisterMessage(GetIngredients)

Ingredients = _reflection.GeneratedProtocolMessageType('Ingredients', (_message.Message,), dict(
  DESCRIPTOR = _INGREDIENTS,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.Ingredients)
  ))
_sym_db.RegisterMessage(Ingredients)

CookIt = _reflection.GeneratedProtocolMessageType('CookIt', (_message.Message,), dict(
  DESCRIPTOR = _COOKIT,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.CookIt)
  ))
_sym_db.RegisterMessage(CookIt)

CookMethod = _reflection.GeneratedProtocolMessageType('CookMethod', (_message.Message,), dict(
  DESCRIPTOR = _COOKMETHOD,
  __module__ = 'recipe_service_pb2'
  # @@protoc_insertion_point(class_scope:recipe.CookMethod)
  ))
_sym_db.RegisterMessage(CookMethod)



_RECIPESERVICE = _descriptor.ServiceDescriptor(
  name='RecipeService',
  full_name='recipe.RecipeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1179,
  serialized_end=1339,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRecipe',
    full_name='recipe.RecipeService.GetRecipe',
    index=0,
    containing_service=None,
    input_type=_GETRECIPEREQUEST,
    output_type=_GETRECIPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateRecipe',
    full_name='recipe.RecipeService.CreateRecipe',
    index=1,
    containing_service=None,
    input_type=_CREATERECIPEREQUEST,
    output_type=_CREATERECIPERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECIPESERVICE)

DESCRIPTOR.services_by_name['RecipeService'] = _RECIPESERVICE

# @@protoc_insertion_point(module_scope)
