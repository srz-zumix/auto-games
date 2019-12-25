# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

from airtest.core.api import *

auto_setup(__file__)

sleep_mul = 1
def pm_sleep(s):
    sleep(s * sleep_mul)

tap_pos = None
def tap():
    if tap_pos:
        touch(tap_pos)

def setup():
    global tap_pos
    if not tap_pos:
        im = exists(Template(r"../../images/feh/tap_normal.png", record_pos=(0.01, 0.741), resolution=(1080, 2160)))
        tap_pos = im


def wait_battle_end():
    result = False
    for i in xrange(50):
        if touch_green():
            break
        else:
            for j in xrange(100):
                tap()
    tap()
    pm_sleep(1)
    for i in xrange(5):
        if not touch_green():
            break
        pm_sleep(1)
    for i in xrange(5):
        if exists(Template(r"../../images/feh/map_select.png", record_pos=(-0.022, -0.494), resolution=(1080, 2160))):
            result = True
            break
        else:
            touch_green()
            pm_sleep(1)
    return result

def touch_green():
    im = exists(Template(r"../../images/feh/positive.png", record_pos=(0.005, 0.266), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    im = exists(Template(r"../../images/feh/positive_close.png", threshold=0.75, record_pos=(0.008, 0.222), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    return False


def open_new_battle():
    im = exists(Template(r"../../images/feh/new_icon.png", threshold=0.7999999999999999, record_pos=(-0.297, -0.206), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    im = exists(Template(r"../../images/feh/quest_cell.png", record_pos=(0.005, -0.117), resolution=(1080, 2160)))
    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    return False

def auto_battle():
    if open_new_battle():
        pm_sleep(0.1)
        if touch_green():
            pm_sleep(3)
            setup()
            wait_battle_end()
    return True

def goto_onsen():
    while auto_battle():
        pass
    pass

goto_onsen()


