from marshmallow import Schema, post_load
from marshmallow import fields as marshmallow_fields
from domain.umishiru.feature import FeatureSchema
from domain.umishiru.field import FieldSchema
from domain.umishiru.spatial_Reference import SpatialReferenceSchema


class GeoSummary:
    def __init__(
        self,
        displayFieldName,
        fieldAliases,
        geometryType,
        spatialReference,
        fields,
        features,
    ):
        self.displayFieldName = displayFieldName
        self.fieldAliases = fieldAliases
        self.geometryType = geometryType
        self.spatialReference = spatialReference
        self.fields = fields
        self.features = features


class GeoSummaryShema(Schema):
    displayFieldName = marshmallow_fields.Str()
    fieldAliases = marshmallow_fields.Dict(
        keys=marshmallow_fields.Str(), values=marshmallow_fields.Str()
    )
    geometryType = marshmallow_fields.Str()
    spatialReference = marshmallow_fields.Nested(SpatialReferenceSchema)
    fields = marshmallow_fields.List(
        marshmallow_fields.Nested(FieldSchema)
    )  # type: ignore
    features = marshmallow_fields.List(marshmallow_fields.Nested(FeatureSchema))

    @post_load
    def make_data(self, data, **kwargs):
        return GeoSummary(**data)
