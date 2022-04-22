#!/usr/bin/env python3
from pyharp.drivers.behavior import Behavior, Events
from pyharp.messages import HarpMessage
from pyharp.messages import MessageType
from struct import *
import os

from pyharp.device import DeviceMode


# Open the device and print the info on screen
# Open serial connection and save communication to a file
device = None
if os.name == 'posix': # check for Linux.
    device = Behavior("/dev/harp_device_00", "ibl.bin")
else: # assume Windows.
    device = Behavior("COM95", "ibl.bin")

print("Setting mode to active.")
# Mode will remain active for up to 3 seconds after CTS pin is brought low.
device.device.set_mode(DeviceMode.Active)
device.disable_all_events()
device.enable_events(Events.port_digital_inputs)
while True:
    event_response = device.device._read() # read any incoming events.
    if event_response is not None:# and event_response.address != 44:
        print()
        print(event_response)
