from marshmallow import Schema, post_load
from marshmallow import fields as marshmallow_fields
from domain.umishiru.feature import Feature, FeatureSchema
from domain.umishiru.field import Field, FieldSchema
from domain.umishiru.spatial_Reference import SpatialReference, SpatialReferenceSchema


class GeoSummary:
    def __init__(
        self,
        displayFieldName: str,
        fieldAliases: dict,
        geometryType: str,
        spatialReference: SpatialReference,
        fields: list[Field],
        features: list[Feature],
        exceededTransferLimit: bool
    ):
        self.displayFieldName = displayFieldName
        self.fieldAliases = fieldAliases
        self.geometryType = geometryType
        self.spatialReference = spatialReference
        self.fields = fields
        self.features = features
        self.exceededTransferLimit = exceededTransferLimit


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
    exceededTransferLimit = marshmallow_fields.Bool(missing=False)  # 送られてくるか不明な項目 既定値

    @post_load
    def make_data(self, data, **kwargs):
        return GeoSummary(**data)
