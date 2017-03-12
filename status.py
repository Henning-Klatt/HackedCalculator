#!/usr/bin/env python
# coding: utf8

import time
#import threading
import psutil
import socket
from datetime import timedelta
import RPi.GPIO as GPIO
import screenmanager
from fonts import font_clean
from display import disp

def lowBat(channel):
    print "Low battery!"

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) #, pull_up_down=GPIO.PUD_DOWN
GPIO.add_event_detect(4, GPIO.FALLING, callback=lowBat, bouncetime=200)
#


class Status:
    def run(self):
        while True:
            free_ram = psutil.virtual_memory()[1]
            print free_ram
            #if((free_ram) < 10000000):
                #disp.reset()
                #disp.begin()
            disp.clear()
            draw = disp.draw()
            uptime = str(timedelta(seconds = float(open('/proc/uptime', 'r').readline().split()[0]))).rsplit('.', 1)[0]
            cpu_usage = str(psutil.cpu_percent())
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('192.168.178.1', 1027))
            ip = s.getsockname()[0]
            s.close()
            screenmanager.draw_text(disp.buffer, "Uptime: ", (0, 250), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, uptime, (0, 200), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, "CPU Load: ", (20, 250), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, cpu_usage + " %", (20, 200), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, "Free RAM: ", (40, 250), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, free_ram, (40, 50), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, "IP: ", (60, 250), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, ip, (60, 50), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, "BT: ", (80, 250), 90, font_clean, fill=(255,255,255))
            screenmanager.draw_text(disp.buffer, str(GPIO.input(4)), (80, 200), 90, font_clean, fill=(255,0,0))
            disp.display()
            time.sleep(1)
