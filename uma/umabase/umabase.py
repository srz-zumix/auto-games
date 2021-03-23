import os

from airtest.core.api import *
from airtest.core.android import *
from time import sleep

class UmaBase:
    def __init__(self, sleep_mul):
        self.sleep_mul = sleep_mul

    def setup(self):
        dev = device()
        if not dev:
            connect_device("Android://")
        dev = device()
        if isinstance(dev, Android):
            dev.touch_method ="ADBTOUCH"

    def set_sleep_mul(self, m):
        self.sleep_mul = m

    def pm_sleep(self, s):
        sleep(s * self.sleep_mul)

    def tap(self):
        touch((80, 1100))

    def touch_training(self):
        touch(Template(r"../../images/uma/training.png", record_pos=(0.001, 0.607), resolution=(1080, 2160)))

    def touch_dayoff(self):
        touch(Template(r"../../images/uma/dayoff.png", record_pos=(-0.333, 0.599), resolution=(1080, 2160)))

    def touch_green(self):
        im = exists(Template(r"../../images/uma/green.png", record_pos=(0.212, 0.728), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        # im = exists(Template(r"../../images/uma/race-green.png", record_pos=(0.149, 0.856), resolution=(1080, 2160)))
        # if im:
        #     pos = (im[0], im[1])
        #     touch(pos)
        #     return True
        return False

    def touch_white(self):
        im = exists(Template(r"../../images/uma/white.png", record_pos=(-0.151, 0.852), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def do_select(self):
        while self.touch_select_green():
            self.pm_sleep(1)
            self.touch_select_yellow()

    def touch_select_green(self):
        im = exists(Template(r"../../images/uma/select-green.png", record_pos=(0.0, 0.106), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def touch_select_yellow(self):
        im = exists(Template(r"../../images/uma/select-yellow.png", record_pos=(0.002, 0.265), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def touch_next(self):
        im = exists(Template(r"../../images/uma/next.png", record_pos=(0.214, 0.869), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def touch_race(self):
        im = self.is_opened_race()
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def touch_goto_race(self):
        im = exists(Template(r"../../images/uma/take-off.png", record_pos=(0.208, 0.704), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def touch_retry(self):
        touch(Template(r"../../images/uma/retry.png", record_pos=(0.22, 0.272), resolution=(1080, 2160)))

    def touch_inherit(self):
        im = exists(Template(r"../../images/uma/inherit.png", record_pos=(0.007, 0.671), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            return True
        return False

    def is_locked_race(self):
        if self.is_opened_race():
            return exists(Template(r"../../images/uma/locked-race.png", threshold=0.9, record_pos=(0.267, 0.791), resolution=(1080, 2160)))
        return False

    def is_opened_race(self):
        return exists(Template(r"../../images/uma/race.png", record_pos=(0.267, 0.791), resolution=(1080, 2160)))

    def is_before_race(self):
        return exists(Template(r"../../images/uma/before-race.png", record_pos=(-0.213, 0.722), resolution=(1080, 2160)))

    def is_briefing_race(self):
        return exists(Template(r"../../images/uma/briefing-race.png", record_pos=(0.083, 0.853), resolution=(1080, 2160)))

    def is_result_race(self):
        return exists(Template(r"../../images/uma/result-race.png", record_pos=(0.098, -0.068), resolution=(1080, 2160)))

    def is_clock(self):
        return exists(Template(r"../../images/uma/clock.png", record_pos=(-0.192, 0.169), resolution=(1080, 2160)))

    def rescue_error(self):
        if exists(Template(r"../../images/uma/error-dialog.png", record_pos=(0.008, 0.006), resolution=(1080, 2160))):
            self.touch_retry()

    def rescue_skipoff(self):
        im = exists(Template(r"../../images/uma/skip-off.png", record_pos=(-0.144, 0.956), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            self.pm_sleep(1)
            touch(pos)
            self.pm_sleep(1)
            return True
        return False


