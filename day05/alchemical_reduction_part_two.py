#!/usr/bin/python
import re

def react_polymer(polymer, remove_unit):
	pattern = re.compile(remove_unit, re.IGNORECASE)
	polymer = pattern.sub('', polymer)

	index = 0
	while index < len(polymer)-1:
		#print "Index " + str(index) + ", char: " + polymer[index]
		#print "Index+1 " + str(index+1) + ", char: " + polymer[index+1]

		# Check if two adjacent 'units' have opposing 'polarities' 
		if (polymer[index].isupper() and polymer[index+1].islower()) or (polymer[index].islower() and polymer[index+1].isupper()):

			# Now check if they are the same type of unit:
			if polymer[index].lower() == polymer[index+1].lower():
				#print "Polarity! " + polymer[index] + " " + polymer[index+1]
				polymer = polymer[:index] + polymer[index+2:]
				#print "new polymer: " + polymer
				index -= 2

		index += 1

	polymer = polymer.rstrip()

	#print "New polymer length: " + str(len(polymer))
	return len(polymer)


fh = open('input.txt', 'r')

original_polymer = fh.readline()
fh.close()

smallest_polymer = len(original_polymer)

for i in range(ord('a'),ord('z')+1):
	reacted_polymer = react_polymer(original_polymer, chr(i))
	if reacted_polymer < smallest_polymer:
		smallest_polymer = reacted_polymer
			
print smallest_polymer
