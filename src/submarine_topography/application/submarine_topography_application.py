import csv
import itertools
import json
from typing import List
from submarine_topography.domain.seafarlen.seafarlen_feature import SeafarlenFeature
from submarine_topography.domain.umishiru.feature_type import FeatureType
from submarine_topography.domain.umishiru.geo_summary import GeoSummary
from submarine_topography.repository.submarin_topography_repository import SubmarineTopographyRepository
import os


class SubmarineTopographyApplication:
    def __init__(self):
        self.__repository = SubmarineTopographyRepository()
        self.__csv_data_path = "data/point_of_submarine_topography.csv"
        self.__insert_submarine_point_sql_path = "data/submarine_topography_insert.sql"
        self.__data_folder_path = "data/submarine_topography/"

    def get_all_point_of_submarine_topography(self) -> GeoSummary:
        return self.__repository.get_all_point_of_submarine_topography()

    def out_all_point_of_submarine_topography_as_csv(self):
        point_of_submarine = self.get_all_point_of_submarine_topography()

        if os.path.isfile(self.__csv_data_path):
            os.remove(self.__csv_data_path)
        with open(self.__csv_data_path, "w", encoding="utf-8", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "海底地形名",
                    "かな",
                    "Undersea_Feature_Name",
                    "属名",
                    "水深",
                    "呼称の由来",
                    "由来_En",
                    "会議名",
                    "JCUFN_approved",
                    "SCUFN_approved",
                    "x",
                    "y"
                ]
            )

            for feature in point_of_submarine.features:
                writer.writerow(
                    [
                        feature.attributes.海底地形名,
                        feature.attributes.かな,
                        feature.attributes.Undersea_Feature_Name,
                        feature.attributes.属名,
                        feature.attributes.水深,
                        feature.attributes.呼称の由来,
                        feature.attributes.由来_En,
                        feature.attributes.会議名,
                        feature.attributes.JCUFN_approved,
                        feature.attributes.SCUFN_approved,
                        feature.geometry.x,
                        feature.geometry.y,
                    ]
                )

    def output_submarine_topography_point_insert_sql(self):
        if not os.path.isfile(self.__csv_data_path):
            raise FileNotFoundError(f"{self.__csv_data_path} not found...")
        if os.path.isfile(self.__insert_submarine_point_sql_path):
            os.remove(self.__insert_submarine_point_sql_path)
        with open(self.__csv_data_path, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)

            with open(self.__insert_submarine_point_sql_path, "w", encoding="utf-8", newline="\n") as f2:
                for row in reader:
                    row = [s.replace("'", "''") for s in row]
                    f2.write(f"INSERT INTO UMISHIRU_UNDERSEA_FEATURE (NAME, \
YOMIGANA, \
UNDERSER_FEATURE_NAME, \
FEATURE_TYPE, DEPTH, \
NAME_ORIGIN, \
ENGLISH_NAME_ORIGIN, \
CONFERENCE, \
JCUFN_APPROVED_YEAR, \
SCUFN_APPROVED_YEAR, \
GEOMETRY_POINT) VALUES (\
'{row[0]}', \
'{row[1]}', \
'{row[2]}', \
{FeatureType.get_numeric_value(row[3])}, \
{row[4] or -1}, \
'{row[5]}', \
'{row[6]}', \
'{row[7]}', \
'{f"{row[8]}/01/01 0:00:00" if row[8] != "" and len(row[8]) == 4 else "1000/01/01 0:00:00"}', \
'{f"{row[9]}/01/01 0:00:00" if row[9] != "" and len(row[9]) == 4 else "1000/01/01 0:00:00"}', \
ST_GeomFromText('POINT({row[10]} {row[11]})', 4326));\n")

    def out_json(self):
        if not os.path.isfile(self.__csv_data_path):
            raise FileNotFoundError("data/submarine_topography.csv not found...")

        features: List[SeafarlenFeature] = []
        with open(self.__csv_data_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)

            for row in reader:
                features.append(SeafarlenFeature(*row))

        features = sorted(features, key=lambda x: x.feature_type.value[0])
        for key, items in itertools.groupby(features, lambda x: x.feature_type.value[0]):
            group_enum = FeatureType.int_to_enum(key)
            out_path = f"{self.__data_folder_path}{group_enum.name.lower()}.geojson"

            if os.path.isfile(out_path):
                os.remove(out_path)

            feature_jsons = [item.to_json() for item in items]
            with open(out_path, 'w', encoding="utf-8") as f:
                data = {"type": "FeatureCollection",
                        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                        "features" : feature_jsons}
                json.dump(data, f, ensure_ascii=False)
