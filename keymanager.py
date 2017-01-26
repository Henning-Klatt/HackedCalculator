#!/usr/bin/env python
# coding: utf8

import time
import click

def run():
    while True:
        if 'key' in locals():
            print "Taste: " + key
            del key
        else:
            key = click.getchar()
        time.sleep(.1)
