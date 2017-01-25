#!/usr/bin/env python
# coding: utf8

import time

def run():
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        print "Beende Programm..."
