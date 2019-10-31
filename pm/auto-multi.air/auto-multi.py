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

def touch_dlg_positive_button():
    im = exists(Template(r"../../images/pm/dlg-restart.png", record_pos=(0.001, 0.889), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        pm_sleep(1)
        return True
    imOk = exists(Template(r"../../images/pm/dlg-ok.png", record_pos=(0.001, 0.889), resolution=(1080, 2160)))
    if imOk:
        pos = (imOk[0], imOk[1])
        touch(pos)
        pm_sleep(1)
        return True
    return False

def touch_matching():
    try:
        im = exists(Template(r"../../images/pm/random-match.png", record_pos=(-0.223, -0.031), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1])
            touch(pos)
            pm_sleep(1)
            return True
    except:
        pass
    return False


def is_quest_select():
    return pm.is_quest_select()

def touch_quest_banner(lv):
    return pm.touch_quest_banner(lv)

def touch_result():
    return pm.touch_result()

def exists_battle():
    imBar = exists(Template(r"../../images/pm/gage.png", record_pos=(-0.002, 0.249), resolution=(1080, 2160)))
    if imBar:
        return imBar
    im = exists(Template(r"../../images/pm/bar2.png", record_pos=(-0.003, 0.935), resolution=(1080, 2160)))
    if im:
        y1 = im[1]
        # if y1 > 1950:
        #     return im
        im = exists(Template(r"../../images/pm/stamp.png", record_pos=(-0.003, 0.935), resolution=(1080, 2160)))
        if im:
            y2 = im[1]
            if abs(y2-y1) < 50:
                return im
    return False

def check_battle():
    im = exists_battle()
    if im:
        pos = (100, im[1])
        touch(pos)
        if touch_dlg_positive_button():
            return False
        pm_sleep(15)
        return True
    return False

def wait_check_battle():
    if check_battle():
        for x in range(5):
            if not check_battle():
                break
        return True
    return False

def wait_battle():
    if not exists(Template(r"../../images/pm/result.png", record_pos=(0.049, 0.641), resolution=(1080, 2160))):
        if not wait_check_battle():
            return
    if touch_result():
        while touch_result():
            pass
        while not touch_positive_button():
            pass
        pm_sleep(1)
        touch_positive_button()
        pm_sleep(6)
        while not is_quest_select():
            pass

def auto_battle(lv):
    while True:
        if touch_quest_banner(lv):
            touch_matching()
            touch_positive_button()
            pm_sleep(30)
        else:
            if not touch_positive_button():
                touch_dlg_positive_button()
        wait_battle()
        # update()

def main():
    auto_battle(1)

main()


