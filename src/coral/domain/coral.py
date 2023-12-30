class Coral:
    def __init__(self, attrubutes: list[str], longitudue: int, latitude: int):
        self.__attribute = attrubutes
        self.__longitude = longitudue
        self.__latitude = latitude

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def attribute(self):
        return self.__attribute
