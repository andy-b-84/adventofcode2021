#!/usr/bin/env python

import os

lines = 0

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

#ones_array = ones_array[::-1]

ones_are_most_common = [0] * len(ones_array)

# get bit criterias
for index, bit in enumerate(ones_array):
    ones_are_most_common[index] = 1 if bit >= ( lines / 2 ) else 0

file_to_grep_oxygen = file_to_grep_co2 = 'input.txt'

pattern = '^'

# grep for bits according to criterias
for index, one_is_most_common in enumerate(ones_are_most_common):
    new_file_to_grep_oxygen = f'input.oxygen.{index}.txt'
    new_file_to_grep_co2 = f'input.co2.{index}.txt'

    pattern += '.'

    os.system(f"grep '{pattern}{one_is_most_common}' {file_to_grep_oxygen} > {new_file_to_grep_oxygen}")
    os.system(f"grep -v '{pattern}{one_is_most_common}' {file_to_grep_co2} > {new_file_to_grep_co2}")

    file_to_grep_oxygen = new_file_to_grep_oxygen
    file_to_grep_co2 = new_file_to_grep_co2

oxygen_file = co2_file = 'input.txt'
oxygen_index_found = co2_index_found = False

# now get the last file from each gas which still has data
for index in range(0, len(ones_array))[::-1]:
    if oxygen_index_found and co2_index_found:
        pass
    else:
        if not oxygen_index_found and os.path.getsize(f'input.oxygen.{index}.txt') > 0:
            oxygen_index_found = True
            oxygen_file = f'input.oxygen.{index}.txt'
        if not co2_index_found and os.path.getsize(f'input.co2.{index}.txt') > 0:
            co2_index_found = True
            co2_file = f'input.co2.{index}.txt'

with open(oxygen_file) as oxygen_file_content:
    oxygen = int(oxygen_file_content.readline(), 2)

with open(co2_file) as co2_file_content:
    co2 = int(co2_file_content.readline(), 2)

print(oxygen*co2)