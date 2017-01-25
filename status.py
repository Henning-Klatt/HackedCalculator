#!/usr/bin/env python
# coding: utf8

import time
import psutil
from datetime import timedelta

from fonts import font_clean

import screenmanager

def run(disp):
    while True:
        disp.clear((0, 0, 0))
        draw = disp.draw()
        uptime = str(timedelta(seconds = float(open('/proc/uptime', 'r').readline().split()[0]))).rsplit('.', 1)[0]
        cpu_usage = str(psutil.cpu_percent())
        screenmanager.draw_text(disp.buffer, "Uptime: ", (0, 250), 90, font_clean, fill=(255,255,255))
        screenmanager.draw_text(disp.buffer, uptime, (0, 200), 90, font_clean, fill=(255,255,255))
        screenmanager.draw_text(disp.buffer, "CPU Load: ", (20, 250), 90, font_clean, fill=(255,255,255))
        screenmanager.draw_text(disp.buffer, cpu_usage + " %", (20, 200), 90, font_clean, fill=(255,255,255))
        disp.display()
        time.sleep(1)
