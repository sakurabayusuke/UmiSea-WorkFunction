import csv
from submarine_topography.domain.umishiru.geo_summary import GeoSummary
from submarine_topography.repository.submarin_topography_repository import SubmarineTopographyRepository
import os


class SubmarineTopographyApplication:
    def __init__(self):
        self.__repository = SubmarineTopographyRepository()

    def get_all_point_of_submarine_topography(self) -> GeoSummary:
        return self.__repository.get_all_point_of_submarine_topography()

    def out_all_point_of_submarine_topography_as_csv(self):
        point_of_submarine = self.get_all_point_of_submarine_topography()

        filepath = "data/point_of_submarine_topograhy.csv"
        if os.path.isfile(filepath):
            os.remove(filepath)
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
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
