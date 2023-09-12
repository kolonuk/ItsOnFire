# Lifted and slightly modded for use case from https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import wifi

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(wifi.ssid, wifi.password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)