#!/usr/bin/env python
# coding: utf8

import time
import click
import sys, os
import threading

import screenmanager

from display import disp

class Keymanager:
    def run(self):
        while True:
            if 'key' in locals():
                print "Taste: " + key
                if(key == "c"):
                    print "Beende Programm..."
                    disp.clear((0, 0, 0))
                    disp.display()
                    os._exit(1)
                if(key == "h"):
                    print "Home Menü"
                    screenmanager.Manager().stopScreen()
                del key
            else:
                key = click.getchar()
            time.sleep(.1)
