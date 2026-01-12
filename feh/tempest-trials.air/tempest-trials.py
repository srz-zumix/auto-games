# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

from airtest.core.api import *
from airtest.core.android import *

auto_setup(__file__)
dev = device()
if not dev:
    connect_device("Android://")
dev = device()
if isinstance(dev, Android):
    dev.touch_method ="ADBTOUCH"

stamina_recovery_pos = (0,0)
banner_pos = (0,0)

sleep_mul = 1
def pm_sleep(s):
    sleep(s * sleep_mul)

def touch_1():
    touch((80, 1100))

def try_touch(method):
    retry = 10
    while not method():
        retry -= 1
        if retry <= 0:
            return False
    return True

def prepare():
    global stamina_recovery_pos
    global banner_pos
    screen = G.DEVICE.snapshot()
    template = Template(r"../../images/feh/stamina-recovery-button.png", record_pos=(0.068, -0.747), resolution=(720, 1496))
    result = template.match_all_in(screen)

    if not result:
        return False
    rectangle = result[0]["rectangle"]
    stamina_recovery_pos = (rectangle[0][0]+10, rectangle[3][1]+10)

    banner = Template(r"../../images/feh/tempest-trials-banner.png", record_pos=(0.013, 0.2), resolution=(720, 1496))
    result = template.match_all_in(screen)

    if not result:
        return False
    rectangle = result[0]["rectangle"]
    banner_pos = ((rectangle[0][0]+rectangle[2][0]) / 2, rectangle[3][0]+80)

    return True

def stamina_recovery():
    touch(stamina_recovery_pos)
    pm_sleep(1)
    im = exists(Template(r"../../images/feh/stamina-recovery.png", record_pos=(-0.003, 0.036), resolution=(720, 1496)))

    if im:
        while not touch_recovery():
            pass
        while not touch_recovery():
            pass
        return True
    return False

def start_auto_loop():
    try_touch(select_auto_loop)
    touch_green()

def select_auto_loop():
    touch(banner_pos)
    pm_sleep(1)
    im = exists(Template(r"../../images/feh/select-auto.png", record_pos=(0.008, 0.224), resolution=(720, 1496)))

    if im:
        touch(Template(r"../../images/feh/select-left.png", record_pos=(-0.256, 0.314), resolution=(720, 1496)))
        return True

    return False


def touch_green():
    im = exists(Template(r"../../images/feh/positive.png", record_pos=(0.001, 0.097), resolution=(720, 1496)))

    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    return False

def touch_recovery():
    im = exists(Template(r"../../images/feh/positive-recovery.png", record_pos=(0.001, 0.097), resolution=(720, 1496)))

    if im:
        pos = (im[0], im[1])
        touch(pos)
        return True
    return False


def auto_battle():
    while True:
        if stamina_recovery():
            pm_sleep(1)
            start_auto_loop()
        pm_sleep(5)

if prepare():
    auto_battle()









