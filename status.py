#!/usr/bin/env python
# coding: utf8

import threading
import time

class Status(object):
    def start(self):
        print "Statusseite gestartet"
        thread = threading.Thread(target=run, args=())
        thread.daemon = True
        thread.start()

    def run():
        while True:
            print('Doing something imporant in the background')
            time.sleep(1)
