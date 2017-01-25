#!/usr/bin/env python
# coding: utf8

import threading
import time
from datetime import timedelta

from fonts import font_clean

import screenmanager

class Status(object):
    def start(self, disp):
        print "Statusseite gestartet"
        thread = threading.Thread(target=run(disp), args=())
        thread.daemon = True
        thread.start()

def run(disp):
    while True:
        disp.clear((0, 0, 0))
        draw = disp.draw()
        uptime = str(timedelta(seconds = float(open('/proc/uptime', 'r').readline().split()[0]))).rsplit('.', 1)[0]
        screenmanager.draw_text(disp.buffer, "Uptime: " + uptime, (0, 220), 90, font_clean, fill=(255,255,255))
        disp.display()
        time.sleep(1)
