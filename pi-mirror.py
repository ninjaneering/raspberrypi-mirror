#!/usr/env/python

import picamera
from time import sleep

camera = picamera.PiCamera()

camera.vflip = False
camera.hflip = False
camera.brightness = 60

camera.start_preview()


while True:
    sleep(1)
