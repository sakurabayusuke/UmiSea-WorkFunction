from marshmallow import Schema, fields, post_load


class Field:
    def __init__(self, name, type, alias, length):
        self.name = name
        self.type = type
        self.alias = alias
        self.length = length


class FieldSchema(Schema):
    name = fields.Str()
    type = fields.Str()
    alias = fields.Str()
    length = fields.Int(missing=None)

    @post_load
    def make_field(self, data, **kwargs):
        return Field(**data)
