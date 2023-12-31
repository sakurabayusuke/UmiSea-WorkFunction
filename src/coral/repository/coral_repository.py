import os
import requests
import numpy as np
from error.exceeded_transfer_limit_error import ExceededTransferLimitError
from error.convert_error import ConvertError
from tqdm import tqdm
from domain.umishiru.geo_summary import GeoSummary, GeoSummaryShema


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

    def get_all_coral(self) -> list[GeoSummary]:
        east_longitude_start = 110.0
        east_longitude_end = 155.0
        north_latitude_start = 10.0
        north_latitude_end = 46.0
        search_height = 0.5
        geoSummaryList = []
        with tqdm(np.arange(north_latitude_start, north_latitude_end + 1, search_height)) as progress_bar:
            for latitude in progress_bar:

                progress_bar.set_description("download")

                where = f"&geometry={east_longitude_start},{latitude},{east_longitude_end},{latitude + search_height}"
                url = self.__url_base + where
                response = requests.get(url, headers=self.__header)
                response.raise_for_status()
                geoSummarySchema = GeoSummaryShema()
                geoSummary = geoSummarySchema.load(response.json())
                if not isinstance(geoSummary, GeoSummary):
                    raise ConvertError("can not convert json Object to GeoSummary")
                if geoSummary.exceededTransferLimit:
                    raise ExceededTransferLimitError("can not all coral data")
                geoSummaryList.append(geoSummary)
        return geoSummaryList
