#!/usr/bin/env python
# coding: utf8

import time
import click

from display import disp

def run():
    while True:
        if 'key' in locals():
            print "Taste: " + key
            if(key == "c"):
                print "Beende Programm..."
                Manager.stopScreen()
                disp.clear((0, 0, 0))
            del key
        else:
            key = click.getchar()
        time.sleep(.1)
