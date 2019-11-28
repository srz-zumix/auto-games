# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

from airtest.core.api import *

auto_setup(__file__)

sleep_mul = 1
def pm_sleep(s):
    sleep(s * sleep_mul)

def touch_1():
    touch((80, 1100))

def touch_banner():
    im = exists(Template(r"../../images/feh/luna.png", record_pos=(-0.076, -0.037), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1] - 50)
        touch(pos)
        return True
    else:
        im = exists(Template(r"../../images/feh/infa.png", record_pos=(-0.07, -0.04), resolution=(1080, 2160)))
        if im:
            pos = (im[0], im[1] - 50)
            touch(pos)
            return True
    return False

def touch_green():
    im = exists(Template(r"../../images/feh/positive.png", record_pos=(0.005, 0.266), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    return False


def wait_event():
    while not exists(Template(r"../../images/feh/auto.png", record_pos=(0.291, 0.825), resolution=(1080, 2160))):
        touch_1()
    pm_sleep(3)

def touch_auto():
    im = exists(Template(r"../../images/feh/auto.png", record_pos=(0.291, 0.825), resolution=(1080, 2160)))
    if im:
        pm_sleep(0.5)
        pos = (im[0], im[1])
        touch(pos)
        pm_sleep(0.1)
        if not touch_green():
            return touch_auto()
        return True
    return False

def wait_battle_end():
    result = False
    for i in xrange(50):
        if exists(Template(r"../../images/feh/clear.png", record_pos=(0.224, 0.029), resolution=(1080, 2160))):
            break
        else:
            pm_sleep(2)
    touch_1()
    pm_sleep(1)
    for i in xrange(5):
        if exists(Template(r"../../images/feh/map_select.png", record_pos=(-0.022, -0.494), resolution=(1080, 2160))):
            result = True
            break
        else:
            pm_sleep(1)
    return result


def auto_battle():
    while True:
        if touch_banner():
            while not touch_green():
                pass
            pm_sleep(4)
        wait_event()
        if touch_auto():
            pm_sleep(5)
            wait_battle_end()

auto_battle()






