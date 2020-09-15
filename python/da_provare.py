#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os
import time
import bluetooth

DEVICES=['D8:BB:2C:85:22:17']
SLEEP_INTERVAL=30

def run():

  # while True:

    print ('In-Out: Checking ' + time.strftime('%Y/%m/%d (%a) %H:%M %Z', time.localtime()))

    for device in DEVICES:
      result = bluetooth.lookup_name(device, timeout=5)
      if (result != None):
        print('In-Out: In: %s (%s)' % (result, device))
        write_in_out()
      else:
        print('In-Out: No Bluetooth device detected: ' + device)

    # time.sleep(SLEEP_INTERVAL)
