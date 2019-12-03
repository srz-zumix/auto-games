# -*- encoding=utf8 -*-
__author__ = "zumix"

from airtest.core.api import *

auto_setup(__file__)

def tap():
    pass

def wait_battle_end():
    result = False
    for i in xrange(50):
        if exists(Template(r"../../images/feh/clear.png", record_pos=(0.224, 0.029), resolution=(1080, 2160))):
            break
        else:
            for j in xrange(20):
                tap()
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
    pass

def goto_onsen():
    pass

goto_onsen()
