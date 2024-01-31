from enum import Enum


class FeatureType(Enum):
    UNDEFINED = (0, "未定義")
    OTHER = (1, "その他")
    BANK = (2, "堆")
    BASIN = (3, "海盆")
    KNOLL = (4, "海丘")
    SPUR = (5, "海脚")
    SUBMARINE_CANYON = (6, "海底谷")
    SEAMOUNT = (7, "海山")
    OBSTACLE = (8, "瀬・根・礁")
    ESCARPMENT = (9, "海底崖")
    TROUGH = (10, "舟状海盆")
    GUYOT = (11, "平頂海山")
    SUBMARINE_GRABEN = (12, "海底地溝")
    HILL = (13, "海陵")
    HOLE = (14, "海穴")
    SADDLE = (15, "鞍部")
    CALDERA = (16, "カルデラ")
    SHELF_CHANNELS = (17, "陸棚谷群")
    HILLS = (18, "海陵群")
    KNOLLS = (19, "海丘群")
    MATA = (20, "周辺凹地")
    FAN = (21, "海底扇状地")
    SEAMOUNTS = (22, "海山群")
    SUBMARINE_CANYONS = (23, "海底谷群")
    RISE = (24, "海膨")
    BANKS = (25, "堆群")
    HILL_CHAIN = (26, "小丘列")
    RIDGE = (27, "海嶺")
    TRENCH = (28, "海溝")
    GAP = (29, "海裂")
    PLATEAU = (30, "海台")
    MUD_VOLCANO = (31, "泥火山")
    CALDRON = (32, "海釜")
    KNOLL_CHAIN = (33, "海丘列")
    FAN_SHINKAI = (34, "深海扇状地")
    SEA_MOUNT_CHAIN = (35, "海山列")
    DEPRESSION = (36, "凹地")

    @classmethod
    def get_numeric_value(cls, name: str) -> int:
        for enum in cls:
            if enum.value[1] == name:
                return enum.value[0]
        return cls.UNDEFINED.value[0]

    @classmethod
    def str_to_enum(cls, name: str) -> 'FeatureType':
        for enum in cls:
            if enum.value[1] == name:
                return enum
        return cls.UNDEFINED

    @classmethod
    def int_to_enum(cls, num: int) -> 'FeatureType':
        for enum in cls:
            if enum.value[0] == num:
                return enum
        return cls.UNDEFINED
