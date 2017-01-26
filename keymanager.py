#!/usr/bin/env python
# coding: utf8

import time

def run():
    try:
        input = raw_input('> ')
        if(input == "exit"):
            print "Beende Programm..."
        else:
            print input
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        print "Beende Programm..."
