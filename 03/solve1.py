#!/usr/bin/env python

# create an array to store how many ones there are in each position
with open('input.txt') as file:
    first_bits = []
    first_line = file.readline()
    ones_array = [0] * ( len(first_line) - 1 ) # fucking \n

# parse the file to find how many ones there are in each position
for lines, line in enumerate(open('input.txt')):
    bits = []
    bits[:0] = line.rstrip("\n")

    position = 0

    for bit in bits:
        ones_array[position] += int(bit)
        position += 1

gamma = 0
epsilon = 0

bit_value = 1

# get gamma and epsilon ratings
for bit in ones_array[::-1]:
    gamma_or_epsilon = bit >= ( lines / 2 )
    gamma += gamma_or_epsilon * bit_value
    epsilon += ( not gamma_or_epsilon ) * bit_value

    bit_value *= 2

print ( gamma * epsilon )