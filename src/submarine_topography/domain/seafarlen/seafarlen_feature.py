from submarine_topography.domain.umishiru.feature_type import FeatureType

class SeafarlenFeature:
    def __init__(self, name, kana, english_name, type_name, depth, origin, origin_en, meeting, jcu_fn_approved, scu_fn_approved, x, y):
        self.name = name
        self.kana = kana
        self.english_name = english_name
        self.feature_type = FeatureType.str_to_enum(type_name)
        depth_value = None
        try:
            depth_value = int(depth)
        except ValueError:
            depth_value = None
        self.depth = depth_value
        self.origin = origin
        self.origin_en = origin_en
        self.meeting = meeting
        self.jcu_fn_approved = jcu_fn_approved
        self.scu_fn_approved = scu_fn_approved
        self.x = x
        self.y = y

    def to_json(self):
        return {
            "type": "Feature",
            "properties": {
                "name": self.name,
                "kana": self.kana,
                "english_name": self.english_name,
                "feature_type": self.feature_type.value[0],
                "depth": self.depth,
                "origin": self.origin,
                "origin_en": self.origin_en,
                "meeting": self.meeting,
                "jcu_fn_approved": self.jcu_fn_approved,
                "scu_fn_approved": self.scu_fn_approved
            },
            "geometry": {
                "type": "Point",
                "coordinates": [float(self.x), float(self.y)]
            }
        }