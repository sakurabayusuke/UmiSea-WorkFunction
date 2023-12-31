import os
import requests
from error.exceeded_transfer_limit_error import ExceededTransferLimitError
from error.convert_error import ConvertError
from submarine_topography.domain.umishiru.geo_summary import GeoSummary, GeoSummarySchema


class SubmarineTopographyRepository:
    def __init__(self):
        api_key = os.environ.get("UMISHIRU_API_KEY")
        if not api_key:
            raise ValueError("[ERROR] not found UMISHIRU_API_KEY")
        self.__header = {"Ocp-Apim-Subscription-Key": api_key}

        self.__url_base = (
            "https://api.msil.go.jp/undersea-features/v2/MapServer/1/query?"
            "f=json&geometryType=esriGeometryEnvelope"
            "&spatialRel=esriSpatialRelIntersects"
            "&units=esriSRUnit_Meter"
            "&returnGeometry=true"
        )

    def get_all_point_of_submarine_topography(self) -> GeoSummary:
        response = requests.get(self.__url_base, headers=self.__header)
        response.raise_for_status()
        geoSummarySchema = GeoSummarySchema()
        geoSummary = geoSummarySchema.load(response.json())
        if not isinstance(geoSummary, GeoSummary):
            raise ConvertError("can not convert json Object to GeoSummary")
        if geoSummary.exceededTransferLimit:
            raise ExceededTransferLimitError("can not all coral data")
        return geoSummary
