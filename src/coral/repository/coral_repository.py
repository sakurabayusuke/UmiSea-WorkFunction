import os
import requests
import numpy as np
from error.convert_error import ConvertError

from domain.geo_summary import GeoSummary, GeoSummaryShema


class CoralRepository:
    def __init__(self):
        api_key = os.environ.get("UMISHIRU_API_KEY")
        if not api_key:
            raise ValueError("[ERROR] not found UMISHIRU_API_KEY")
        self.__header = {"Ocp-Apim-Subscription-Key": api_key}

        self.__url_base = (
            "https://api.msil.go.jp/coral/v2/MapServer/1/query?f=json"
            "&geometryType=esriGeometryEnvelope"
            "&spatialRel=esriSpatialRelIntersects"
            "&units=esriSRUnit_Meter"
            "&returnGeometry=true"
        )

    def get_all_coral(self):
        east_longitude_start = 110.0
        east_longitude_end = 155.0
        search_wide = 0.5
        north_latitude_start = 10.0
        north_latitude_end = 46.0
        search_height = 0.5
        for latitude in np.arange(north_latitude_start, north_latitude_end + 1, search_height):
            for longitude in np.arange(east_longitude_start, east_longitude_end + 1, search_wide):
                where = f"&geometry={longitude},{latitude},{longitude + search_wide},{latitude + search_height}"
                url = self.__url_base + where
                response = requests.get(url, headers=self.__header)
                response.raise_for_status()
                geoSummarySchema = GeoSummaryShema()
                geoSummary = geoSummarySchema.load(response.json())
                if not isinstance(geoSummary, GeoSummary):
                    raise ConvertError("can not convert json Object to GeoSummary")
                # 疲れた寝る。
