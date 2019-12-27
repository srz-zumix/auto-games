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
        return exists(Template(r"../../images/pm/banner.png", record_pos=(0.004, -0.218), resolution=(1080, 2160), threshold=0.6, rgb=False))

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
                elif lv == 4:
                    touch(Template(r"../../images/pm/super-expert.png", record_pos=(-0.317, -0.446), resolution=(1080, 2160)))
                self.pm_sleep(1)
                return True
        except:
            pass
        return False

    def touch_positive_button(self):
        imOk = exists(Template(r"../../images/pm/ok.png", record_pos=(0.001, 0.889), resolution=(1080, 2160)))
        if imOk:
            pos = (imOk[0], imOk[1] - 28)
            touch(pos)
            self.pm_sleep(1)
            return True
        return False

    def touch_oncemore_button(self):
        imOk = exists(Template(r"../../images/pm/once-more.png", record_pos=(0.22, 0.896), resolution=(1080, 2160)))
        if imOk:
            pos = (imOk[0], imOk[1] - 28)
            touch(pos)
            self.pm_sleep(1)
            return True
        return False

    def touch_result(self):
        imBg = exists(Template(r"../../images/pm/result.png", record_pos=(0.049, 0.641), resolution=(1080, 2160)))
        if imBg:
            try:
                pos = (imBg[0], imBg[1])
                touch(pos)
                self.pm_sleep(0.1)
                return True
            except:
                pass
        return False

    def step_result(self):
        if self.touch_result():
            while self.touch_result():
                self.pm_sleep(0.5)
                self.touch_positive_button()
            while not self.touch_oncemore_button():
                if not self.touch_positive_button():
                    while self.touch_result():
                        pass
            self.pm_sleep(6)
            if self.is_quest_select():
                return "lose"
            return "win"
        return None

    def exists_battle_symbol(self):
        im = exists(Template(r"../../images/pm/bar2.png", record_pos=(-0.003, 0.935), resolution=(1080, 2160)))
        if im:
            y1 = im[1]
            im = exists(Template(r"../../images/pm/speed-and-auto.png", record_pos=(0.328, -0.949), resolution=(1080, 2160)))
            if im:
                y2 = im[1]
                if abs(y2-y1) > 600:
                    return im
        return False

