# -*- encoding=utf8 -*-
__author__ = "srz_zumix"

sys.path.append(r"../pmbase")

from airtest.core.api import *
from pmbase import PmBase

auto_setup(__file__)

# adb = ADB()
# def update():
#    print adb.shell('dumpsys battery')

sleep_mul = 1

class Runner:

    def __init__(self):
        self.pm = PmBase(sleep_mul)
        self.pm.setup()
        self.ok_btn = None
        self.dlg_ok_btn = None

    def pm_sleep(self, s):
        self.pm.pm_sleep(s)

    def ok(self):
        if self.ok_btn:
            pos = (self.ok_btn[0], self.ok_btn[1])
            touch(pos)
        else:
            self.ok_btn = self.pm.touch_positive_button()

    def dlg_ok(self):
        if self.dlg_ok_btn:
            pos = (self.dlg_ok_btn[0], self.dlg_ok_btn[1])
            touch(pos)
        else:
            self.dlg_ok_btn = self.pm.touch_dlg_positive_button()

    def find_first(self):
        self.first_cell = exists(Template(r"../../images/pm/exp-cell.png", record_pos=(-0.336, -0.316), resolution=(1080, 2160), rgb=False))
        return self.first_cell

    def loop_expup(self):
        pos = (self.first_cell[0], self.first_cell[1])
        touch(pos)
        self.pm_sleep(1)
        self.ok()
        self.pm_sleep(1)
        self.ok()
        self.pm_sleep(1)
        self.dlg_ok()
        self.pm_sleep(2)
        self.ok()
        self.pm_sleep(1)
        return True

    def expup(self):
        if self.find_first():
            while self.loop_expup():
                pass

def main():
    r = Runner()
    r.expup()

main()











