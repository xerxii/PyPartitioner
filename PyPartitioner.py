#!usr/bin/env python3.6
# -*- coding: utf-8 -*-


#############################################################
# This program is meant to be loaded in an interpreter      #
# and not intended to be ran as a stand alone program.      #
#                                                           #
# Please copy and paste into iPython or run with python as  #
# python3.6 -i PyPartitioner.py                             #
#                                                           #
#############################################################

# This requires libparted-dev as a dependency for C code, and 
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

# Interpreter based starting steps below, the PyParted PDF may be able to assist you
# Get devices instance by path
# sda = parted.getDevice('/dev/sda')
# disk_model = sda.model


# This function is to get all of the information we need in one sweep
def get_disk_info(path):

    disk = parted.getDevice(path) 
    print(f"Now getting information from the object found at {disk.path!s}\n")
    
    print(f"The disk model of the selected object is: {disk.model!s}")
    print(f"The disk size of the selected object in MB is: {disk.getSize()!s}")
    
    if disk.busy:
        print("The partition object is currently busy")
    else:
        print("The partition object is currently not busy")
        
    if disk.readOnly:
        print("The device is currently read only")
    else:
        print("The device is not read only")    
        
    print(f"The physical sector size of the disk object is: {disk.physicalSectorSize!s}")    
    
    print(get_disk_geometry(disk))
    print(get_bios_geometry(disk))
    
def get_disk_geometry(disk_obj):
     return f"The cynlinders, heads, and sectors of the hardware Geometry is: {disk_obj.hardwareGeometry!s}"

def get_bios_geometry(disk_obj):
     return f"The cynlinders, heads, and sectors of the bios Geometry is: {disk_obj.biosGeometry!s}" 


def destroy_partition_table(path_to_disk):
    
    disk = parted.getDevice(path_to_disk)

    answer = input("WARNING!! You are about to destroy the given partition! Continue? y/n")
    if (answer == 'y'):
        print("Now destroying the partition signatures and partition")
        return disk.clobber, disk.destroy
    elif (answer == 'n'):
        print("Canceling partition destruction")
    else:
        print("Invalid input, please use just 'y' or 'n'")   
        
        
