#!/usr/bin/python

input_file = open('input.txt', 'r')
frequency = 0
for line in input_file:
	frequency += int(line)

print frequency
