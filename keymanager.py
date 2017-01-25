#!/usr/bin/env python
# coding: utf8

import time

def run(self):
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        print "Beende Programm..."
