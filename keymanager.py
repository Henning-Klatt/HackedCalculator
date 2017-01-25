#!/usr/bin/env python
# coding: utf8

import time

def run():
    print "Keylistener aktiviert!"
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        print "Beende Programm..."
