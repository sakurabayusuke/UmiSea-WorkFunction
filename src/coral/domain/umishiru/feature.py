from marshmallow import Schema, fields, post_load
from domain.umishiru.attribute import Attribute, AttributeSchema
from domain.umishiru.geometry import Geometry, GeometrySchema


class Feature:
    def __init__(self, attributes: Attribute, geometry: Geometry):
        self.attributes = attributes
        self.geometry = geometry


class FeatureSchema(Schema):
    attributes = fields.Nested(AttributeSchema)
    geometry = fields.Nested(GeometrySchema)

    @post_load
    def make_feature(self, data, **kwargs):
        return Feature(**data)
