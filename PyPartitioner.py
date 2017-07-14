#!usr/bin/env python3.6
# -*- coding: utf-8 -*-

# This requires libparted-dev as a dependency
# pip3.6 install pyparted  
# this program requires root privelages to interact with the Kernel
# Intended for GNU/Linux only
# There is a general outline of the process at top, with functions to help automate the process below

# *WARNING*
# Partitioning your drive may bring data loss.

# Begin module importing
import parted, os, sys

# Check system compatibility
if sys.platform.startswith("win"):
    raise SystemError("This partitioner is only for GNU/Linux until safer code is written for Windows")
else:
    print("Welcome to PyPartitioner!")

# Get all devices
# This will be a global variable used in the program
list_of_devices = [dev.path for dev in parted.getAllDevices()]

# Interpreter based seteps below, the PyParted PDF may be able to assist you
# Get devices instance by path
sda = parted.getDevice('/dev/sda')
disk_model = sda.model


def get_disk_info(path):
    disk = parted.getDevice(path)
    disk_model = disk.model
    print(f"The disk model is {disk_model!s}")
    
    get_disk_geometry(disk)
    get_bios_geometry(disk)
    
def get_disk_geometry(disk_obj):
     print("The cynlinders, heads, and sectors of the hardware Geometry is...")
     print(f"{disk_obj.hardwareGeometry!s}")

def get_bios_geometry(disk_obj):
     print("The cynlinders, heads, and sectors of the bios Geometry is...")
     print(f"{disk_obj.biosGeometry!s}")
 

