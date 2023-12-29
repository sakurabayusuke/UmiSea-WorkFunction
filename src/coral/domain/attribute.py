from marshmallow import Schema, fields, post_load


class Attribute:
    def __init__(self, 底質):
        self.底質 = 底質


class AttributeSchema(Schema):
    底質 = fields.Str()

    @post_load
    def make_attribute(self, data, **kwargs):
        return Attribute(**data)
