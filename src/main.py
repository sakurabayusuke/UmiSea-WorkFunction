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


def menu(stdscr):
    curses.curs_set(0)
    current_row = 0
    menu = Application.get_values()

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
            selected = menu[current_row]
            break
    if selected == Application.SUBMARINE_TOPOGRAPHY.value:
        SubmarineTopographyApplication().out_all_point_of_submarine_topography_as_csv()
    elif selected == Application.CORAL.value:
        CoralApplication().out_all_coral_as_csv()


curses.wrapper(menu)
