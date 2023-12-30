import csv
from domain.coral import Coral
from domain.umishiru.geo_summary import GeoSummary
from repository.coral_repository import CoralRepository
from tqdm import tqdm
import os


class CoralApplication:
    def __init__(self):
        self.__repository = CoralRepository()

    def get_all_coral_from_umishiru(self) -> list[GeoSummary]:
        return self.__repository.get_all_coral()

    def out_all_coral_as_csv(self):
        umishiru_corals = self.get_all_coral_from_umishiru()
        corals: list[Coral] = []

        for umi_coral in umishiru_corals:
            for coral_detail in umi_coral.features:
                coral = Coral(coral_detail.attributes.底質,
                              coral_detail.geometry.x,
                              coral_detail.geometry.y)
                corals.append(coral)

        filepath = "data/coral.csv"
        if os.path.isfile(filepath):
            os.remove(filepath)
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(["底質", "経度", "緯度"])

            with tqdm(corals) as progres_bar:
                for coral in progres_bar:
                    progres_bar.set_description("csv output")
                    writer.writerow([coral.attribute, coral.longitude, coral.latitude])
