# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

sys.path.append(r"../pmbase")

from airtest.core.api import *
from airtest.core.android import *
from pmbase import PmBase
import datetime
import codecs

auto_setup(__file__)
dev = device()
if isinstance(dev, Android):
    dev.touch_method ="ADBTOUCH"

# adb = ADB()
# def update():
#    print adb.shell('dumpsys battery')

class Logger:
    def __init__(self, path):
        self.path = path

    def log(self, message):
        with codecs.open(self.path, 'a', 'utf-8') as f:
            f.write(message + "\n")


sleep_mul = 1
pm = PmBase(sleep_mul)

now = datetime.datetime.now()
logger = Logger("./log/{0:%Y%m%d_%H%M%S}.txt".format(now))

def pm_sleep(s):
    pm.pm_sleep(s)

def touch_positive_button():
    return pm.touch_positive_button()

def touch_oncemore_button():
    return pm.touch_oncemore_button()

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
            logger.log("match");
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
    if not pm.is_result_bg():
        if not wait_check_battle():
            return
    r = pm.step_result()
    if r:
        logger.log(r)

def auto_battle(lv):
    if touch_quest_banner(lv):
        touch_matching()
        touch_positive_button()
        pm_sleep(30)
    if not touch_positive_button():
        touch_dlg_positive_button()
        touch_oncemore_button()
    while True:
        wait_battle()
        if is_quest_select():
            break
        else:
            if not touch_positive_button():
                touch_positive_button()
            touch_oncemore_button()

def auto_select_battle(lv):
    while True:
        auto_battle(lv)

def main():
    auto_select_battle(3)

main()
