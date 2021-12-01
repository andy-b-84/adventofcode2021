#!/usr/bin/env python

increases = 0

with open('input.txt') as input:
    depthText = input.readline()
    depth1 = int(depthText)
    depthText = input.readline()
    depth2 = int(depthText)
    depthText = input.readline()
    depth3 = int(depthText)

    depthSumOld = depth1 + depth2 + depth3

    while depthText:
        depth3 = int(depthText)
        depthSum = depth1 + depth2 + depth3

        increases += int(depthSum>depthSumOld)

        depthSumOld = depthSum
        depth1 = depth2
        depth2 = depth3
        
        depthText = input.readline() 

print(increases)