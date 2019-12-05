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

def touch_oncemore_button():
    return pm.touch_oncemore_button()

def is_quest_select():
    return pm.is_quest_select()

def touch_quest_banner(lv):
    return pm.touch_quest_banner(lv)

def touch_result():
    return pm.touch_result()

def check_bar():
    im = pm.exists_battle_symbol()
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
        while not touch_oncemore_button():
            touch_positive_button()
            pass
        pm_sleep(6)

def auto_battle(lv):
    # once
    if touch_quest_banner(lv):
        touch_positive_button()
        pm_sleep(10)
    else:
        touch_positive_button()
    while True:
        wait_battle()
        if is_quest_select():
            break
        else:
            touch_positive_button()

def auto_select_battle(lv):
    while True:
        auto_battle(lv)

def main():
    auto_select_battle(4)

main()

