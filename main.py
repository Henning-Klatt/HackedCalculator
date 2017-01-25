#!/usr/bin/env python
# coding: utf8

from screenmanager import Manager

DC = 18
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))
disp.begin()
disp.clear()

Manager.startScreen(disp)
