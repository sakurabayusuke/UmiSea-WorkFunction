from enum import Enum
from submarine_topography.application.submarine_topography_application import SubmarineTopographyApplication
from coral.application.coral_application import CoralApplication
import curses


class Application(Enum):
    CORAL = "Coral"
    SUBMARINE_TOPOGRAPHY = "Submarine Topography"

    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]


class SubmarineTopographyApp(Enum):
    OUT_ALL_POINT_OF_SUBMARINE_TOPOGRAPHY_CSV = "out_all_point_of_submarine_topography_as_csv"
    OUTPUT_SUBMARINE_TOPOGRAPHY_POINT_INSERT_SQL = "output_submarine_topography_point_insert_sql"

    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]


class CoralApp(Enum):
    OUT_ALL_CORALS_CSV = "out_all_coral_as_csv"
    OUTPUT_CORAL_INSERT_SQL = "output_coral_insert_sql"

    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]


def display(stdscr, menu: list[str]) -> str:
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()

        for i, row in enumerate(menu):
            if i != current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(i, 0, row)
                stdscr.attroff(curses.color_pair(1))
                continue
            stdscr.addstr(i, 0, row)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row == 0:
            current_row = len(menu) - 1
        elif key == curses.KEY_DOWN and current_row == len(menu) - 1:
            current_row = 0
        elif key == curses.KEY_UP:
            current_row -= 1
        elif key == curses.KEY_DOWN:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enterキーが押されたら終了
            return menu[current_row]
            break


def menu(stdscr):
    selected_app = display(stdscr, Application.get_values())
    if selected_app == Application.SUBMARINE_TOPOGRAPHY.value:
        selected_method = display(stdscr, SubmarineTopographyApp.get_values())
        submarine_app = SubmarineTopographyApplication()
        if selected_method == SubmarineTopographyApp.OUT_ALL_POINT_OF_SUBMARINE_TOPOGRAPHY_CSV.value:
            submarine_app.out_all_point_of_submarine_topography_as_csv()
        if selected_method == SubmarineTopographyApp.OUTPUT_SUBMARINE_TOPOGRAPHY_POINT_INSERT_SQL.value:
            submarine_app.output_submarine_topography_point_insert_sql()
    elif selected_app == Application.CORAL.value:
        selected_method = display(stdscr, CoralApp.get_values())
        coral_app = CoralApplication()
        if selected_method == CoralApp.OUT_ALL_CORALS_CSV.value:
            coral_app.out_all_coral_as_csv()
        if selected_method == CoralApp.OUTPUT_CORAL_INSERT_SQL.value:
            coral_app.output_coral_insert_sql()


curses.wrapper(menu)
