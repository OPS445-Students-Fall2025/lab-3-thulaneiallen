#!/usr/bin/env python3
'''Lab 3 Inv 2 free_space function'''
# Author ID: Thulanei Allen

import subprocess

def free_space():
    # Run the system command
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Decode to utf-8 and strip newlines/spaces
    return result.stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
