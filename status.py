#!/usr/bin/env python
# coding: utf8

import threading
import time

class Status(object):
    def start(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print('Doing something imporant in the background')
            time.sleep(self.interval)

#example = Status()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')
