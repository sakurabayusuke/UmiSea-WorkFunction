from marshmallow import Schema, fields, post_load


class SpatialReference:
    def __init__(self, wkid, latestWkid):
        self.wkid = wkid
        self.latestWkid = latestWkid


class SpatialReferenceSchema(Schema):
    wkid = fields.Int()
    latestWkid = fields.Int()

    @post_load
    def make_spatial_reference(self, data, **kwargs):
        return SpatialReference(**data)


class SpatialReferenceSchema2(Schema):
    wkid = fields.Int()
    latestWkid = fields.Int()

    @post_load
    def make_spatial_reference(self, data, **kwargs):
        return SpatialReference(**data)
