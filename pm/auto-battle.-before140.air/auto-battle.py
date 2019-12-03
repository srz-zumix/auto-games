# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

sys.path.append(r"../pmbase")

from airtest.core.api import *
from airtest.core.android.adb import *
from pmbase import PmBase

auto_setup(__file__)

# adb = ADB()
# def update():
#    print adb.shell('dumpsys battery')

sleep_mul = 1
pm = PmBase(sleep_mul)

def pm_sleep(s):
    pm.pm_sleep(s)

def touch_positive_button():
    return pm.touch_positive_button()

def is_quest_select():
    return pm.is_quest_select()

def touch_quest_banner(lv):
    return pm.touch_quest_banner(lv)

def touch_result():
    return pm.touch_result()

def check_bar():
    im = exists(Template(r"../../images/pm/bar2.png", record_pos=(-0.003, 0.935), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        pm_sleep(10)
        return True
    return False

def is_wait_bar():
    if check_bar():
        if check_bar():
            check_bar()
        return True
    return False

def wait_battle():
    if not exists(Template(r"../../images/pm/result.png", record_pos=(0.049, 0.641), resolution=(1080, 2160))):
        if not is_wait_bar():
            return
    if touch_result():
        while touch_result():
            pass
        while not touch_positive_button():
            pass
        pm_sleep(6)
        while not is_quest_select():
            pass

def auto_battle(lv):
    while True:
        if touch_quest_banner(lv):
            touch_positive_button()
            pm_sleep(10)
        else:
            touch_positive_button()
        wait_battle()
        # update()

def main():
    auto_battle(4)

main()

