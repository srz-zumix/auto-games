# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

from airtest.core.api import *
from airtest.core.android.adb import *

auto_setup(__file__)

# adb = ADB()
# def update():
#    print adb.shell('dumpsys battery')

sleep_mul = 1
def pm_sleep(s):
    sleep(s * sleep_mul)

def touch_positive_button():
    imOk = exists(Template(r"../../images/pm/ok.png", record_pos=(0.001, 0.889), resolution=(1080, 2160)))
    if imOk:
        pos = (imOk[0], imOk[1] - 28)
        touch(pos)
        pm_sleep(1)
        return True
    return False

def touch_quest_banner(lv):
    try:
        if exists(Template(r"../../images/pm/banner.png", record_pos=(0.004, -0.218), resolution=(1080, 2160))):
            if lv == 0:
                touch(Template(r"../../images/pm/normal.png", record_pos=(-0.335, 0.16), resolution=(1080, 2160)))
            elif lv == 1:
                touch(Template(r"../../images/pm/hard.png", record_pos=(-0.33, -0.145), resolution=(1080, 2160)))
            elif lv == 2:
                touch(Template(r"../../images/pm/very-hard.png", record_pos=(-0.324, -0.45), resolution=(1080, 2160)))
            pm_sleep(1)
            return True
    except:
        pass
    return False

def touch_result():
    imBg = exists(Template(r"../../images/pm/result.png", record_pos=(0.049, 0.641), resolution=(1080, 2160)))
    if imBg:
        try:
            pos = (imBg[0], imBg[1])
            touch(pos)
            sleep(0.1)
            return True
        except:
            pass
    return False

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
    auto_battle(2)

main()





