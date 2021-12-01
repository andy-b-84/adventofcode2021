#!/usr/bin/env python

increases = 0

with open('input.txt') as input:
    depthText = input.readline()
    oldDepth = int(depthText)
    depthText = input.readline()
    depth = int(depthText)
    while depthText:
        depth = int(depthText)
        increases += int(depth>oldDepth)
        oldDepth = depth
        depthText = input.readline() 

print(increases)