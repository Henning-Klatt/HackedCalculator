#!/usr/bin/env python
# coding: utf8

import threading
import time
import psutil
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
        cpu_usage = psutil.cpu_percent()
        screenmanager.draw_text(disp.buffer, "Uptime: " + uptime, (0, 220), 90, font_clean, fill=(255,255,255))
        screenmanager.draw_text(disp.buffer, "CPU Load: " + cpu_usage, (20, 220), 90, font_clean, fill=(255,255,255))
        disp.display()
        time.sleep(1)
