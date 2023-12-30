from marshmallow import Schema, fields, post_load


class Geometry:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GeometrySchema(Schema):
    x = fields.Float()
    y = fields.Float()

    @post_load
    def make_geometry(self, data, **kwargs):
        return Geometry(**data)
