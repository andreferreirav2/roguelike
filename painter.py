from libtcod import libtcodpy as libtcod
from consts import *


class Painter:
    __painter = None

    @staticmethod
    def get_instance():
        if Painter.__painter is None:
            Painter()
        return Painter.__painter

    def __init__(self):
        # Secondary console to draw on
        self.con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

        Painter.__painter = self

    def draw_object(self, x, y, char, color, visible):
        if visible:
            libtcod.console_set_default_foreground(self.con, color)
            libtcod.console_put_char(self.con, x, y, char, libtcod.BKGND_NONE)

    def draw_tile(self, x, y, wall, visible, seen):
        if seen:
            if wall:
                # Draw wall
                if visible:
                    libtcod.console_put_char_ex(self.con, x, y, '#', libtcod.darkest_gray, libtcod.darkest_yellow)
                else:
                    libtcod.console_put_char_ex(self.con, x, y, '#', libtcod.darkest_gray, libtcod.black)
            else:
                # Draw floor
                if visible:
                    libtcod.console_put_char_ex(self.con, x, y, ' ', libtcod.white, libtcod.light_yellow)
                else:
                    libtcod.console_put_char_ex(self.con, x, y, ' ', libtcod.white, libtcod.darker_gray)

    def flush(self):
        libtcod.console_blit(self.con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()
