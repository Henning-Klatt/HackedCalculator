#!/usr/bin/env python
# coding: utf8

import time

def run():
    try:
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        print "Beende Programm..."
