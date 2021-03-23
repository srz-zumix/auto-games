# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

sys.path.append(r"../umabase")

from airtest.core.api import *
from umabase import UmaBase

auto_setup(__file__)

sleep_mul = 1
uma = UmaBase(sleep_mul)

uma.setup()

def pm_sleep(s):
    uma.pm_sleep(s)


def rescue():
    uma.rescue_error()
    uma.rescue_skipoff()


def do_race():
    while not uma.is_briefing_race():
        uma.touch_green()
        uma.pm_sleep(1)
    while not uma.is_result_race():
        uma.touch_white()
        uma.pm_sleep(3)
        uma.tap()
        uma.pm_sleep(2)
        if uma.is_clock():
            print("end...")
            sys.exit(0)
        uma.touch_green()
    while uma.is_result_race():
        uma.touch_next()
        uma.pm_sleep(1)


def make_debut_turn():
    if uma.is_locked_race():
        uma.touch_dayoff()
        uma.pm_sleep(2)
    uma.do_select()


def do_ms_race():
    while uma.is_before_race():
        uma.touch_goto_race()
        uma.pm_sleep(1)
        uma.touch_green()
        uma.pm_sleep(1)
    do_race()


def make_debut():
    rescue()
    while True:
        make_debut_turn()
        rescue()
        if uma.is_before_race():
            do_ms_race()
            return
        uma.touch_green()


def race_turn():
    if uma.is_opened_race():
        while uma.is_opened_race():
            uma.touch_race()
            uma.pm_sleep(1)
            uma.touch_green()
        do_race()
        uma.do_select()
        return True
    uma.do_select()
    return False

def race_turns():
    while race_turn():
        pass
    rescue()
    uma.touch_green()
    uma.touch_inherit()

def loop_race():
    rescue()
    while not uma.is_before_race():
        race_turns()
    do_ms_race()


def auto_mani():
    #make_debut()
    loop_race()

def main():
    auto_mani()

main()



