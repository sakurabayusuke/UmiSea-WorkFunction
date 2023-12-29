from repository.coral_repository import CoralRepository


class CoralApplication:
    def __init__(self):
        self.__repository = CoralRepository()

    def out_all_coral_as_csv(self):
        data = self.__repository.get_all_coral()
        # csv に変換処理