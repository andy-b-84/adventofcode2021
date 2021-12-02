#!/usr/bin/env python

with open('input.txt') as input:
    instruction = input.readline()
    
    depth=0
    distance=0

    while instruction:
        instruction = instruction.split(' ', 3)

        length = int(instruction[1])

        if ('up' == instruction[0]):
            depth-=length
        elif ('down' == instruction[0]):
            depth+=length
        else:
            distance+=length
        
        instruction = input.readline() 

print(depth*distance)