#!/usr/bin/env python
# coding: utf8

import time
import click
import sys

from display import disp

def run():
    while True:
        if 'key' in locals():
            print "Taste: " + key
            if(key == "c"):
                print "Beende Programm..."
                disp.clear((0, 0, 0))
                sys.exit(1)
            del key
        else:
            key = click.getchar()
        time.sleep(.1)
