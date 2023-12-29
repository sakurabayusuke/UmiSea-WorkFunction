from marshmallow import Schema, fields, post_load
from domain.attribute import AttributeSchema
from domain.geometry import GeometrySchema


class Feature:
    def __init__(self, attributes, geometry):
        self.attributes = attributes
        self.geometry = geometry


class FeatureSchema(Schema):
    attributes = fields.Nested(AttributeSchema)
    geometry = fields.Nested(GeometrySchema)

    @post_load
    def make_feature(self, data, **kwargs):
        return Feature(**data)
