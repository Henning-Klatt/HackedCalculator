#!/usr/bin/env python
# coding: utf8

import time
import threading

class Keymanager(object):
    def start(self):
        print "Key listener aktiviert!"
        thread = threading.Thread(target=run(), args=())
        thread.daemon = True
        thread.start()

def run():
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        print "Beende Programm..."
