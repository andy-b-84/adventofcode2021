#!/usr/bin/env python

with open('input.txt') as input:
    instruction = input.readline()
    
    depth=0
    distance=0
    aim=0

    while instruction:
        instruction = instruction.split(' ', 3)

        number = int(instruction[1])

        if ('up' == instruction[0]):
            aim-=number
        elif ('down' == instruction[0]):
            aim+=number
        else:
            distance+=number
            depth+=(aim*number)
        
        instruction = input.readline() 

print(depth*distance)