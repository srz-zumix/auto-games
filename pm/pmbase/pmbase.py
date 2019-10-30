import os

from airtest.core.api import *
from time import sleep

class PmBase:
    def __init__(self, sleep_mul):
        self.sleep_mul = sleep_mul

    def set_sleep_mul(self, m):
        self.sleep_mul = m

    def pm_sleep(self, s):
        sleep(s * self.sleep_mul)

    def is_quest_select(self):
        return exists(Template(r"../../images/pm/banner.png", record_pos=(0.004, -0.218), resolution=(1080, 2160)))

    def touch_quest_banner(self, lv):
        try:
            if self.is_quest_select():
                if lv == 0:
                    touch(Template(r"../../images/pm/normal.png", record_pos=(-0.335, 0.16), resolution=(1080, 2160)))
                elif lv == 1:
                    touch(Template(r"../../images/pm/hard.png", record_pos=(-0.33, -0.145), resolution=(1080, 2160)))
                elif lv == 2:
                    touch(Template(r"../../images/pm/very-hard.png", record_pos=(-0.324, -0.45), resolution=(1080, 2160)))
                elif lv == 3:
                    touch(Template(r"../../images/pm/expert.png", record_pos=(-0.324, -0.45), resolution=(1080, 2160)))
                self.pm_sleep(1)
                return True
        except:
            pass
        return False


