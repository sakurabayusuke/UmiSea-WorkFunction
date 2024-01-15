import csv
import json
from coral.domain.coral import Coral
from coral.domain.umishiru.geo_summary import GeoSummary
from coral.repository.coral_repository import CoralRepository
from tqdm import tqdm
import os


class CoralApplication:
    def __init__(self):
        self.__repository = CoralRepository()
        self.__csv_data_path = "data/coral.csv"
        self.__insert_sql_path = "data/coral_insert.sql"
        self.__json_data_path = "data/coral.json"

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

        if os.path.isfile(self.__csv_data_path):
            os.remove(self.__csv_data_path)
        with open(self.__csv_data_path, "w", encoding="utf-8", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(["底質", "経度", "緯度"])

            with tqdm(corals) as progres_bar:
                for coral in progres_bar:
                    progres_bar.set_description("csv output")
                    writer.writerow([coral.attribute, coral.longitude, coral.latitude])

    def output_coral_insert_sql(self):
        if not os.path.isfile(self.__csv_data_path):
            raise FileNotFoundError("data/coral.csv not found...")
        if os.path.isfile(self.__insert_sql_path):
            os.remove(self.__insert_sql_path)
        with open(self.__csv_data_path, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)

            with open(self.__insert_sql_path, "w", encoding="utf-8", newline="\n") as f2:
                for row in reader:
                    f2.write(f"INSERT INTO UMISHIRU_CORALS (COORDINATE) VALUES (ST_GeomFromText('POINT({row[1]} {row[2]})', 4326));\n")

    def csv_to_json(self):
        if not os.path.isfile(self.__csv_data_path):
            raise FileNotFoundError("data/coral.csv not found...")
        if os.path.isfile(self.__insert_sql_path):
            os.remove(self.__insert_sql_path)

        with open(self.__csv_data_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)

            with open(self.__json_data_path, 'w', encoding="utf-8") as f:
                data = []
                for row in reader:
                    dic = {"type": "Feature", "properties": {"bottom_material": list(row[0].split(","))}, "geometry": {"type": "Point", "coordinates" : [row[1], row[2]]}}
                    data.append(dic)

                data = {"type": "FeatureCollection",
                        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                        "features" : data}
                json.dump(data, f, ensure_ascii=False)