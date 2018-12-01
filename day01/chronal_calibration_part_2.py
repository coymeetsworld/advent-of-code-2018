#!/usr/bin/python



input_file = open('input.txt', 'r')
past_frequencies = set([])

frequency = 0
past_frequencies.add(frequency)
found_duplicate_frequency = None

while True:
	for line in input_file:
		frequency += int(line)
		if frequency in past_frequencies:
			found_duplicate_frequency = frequency
			break
		past_frequencies.add(frequency)

	if found_duplicate_frequency is not None:
		break
	input_file.seek(0) # if no frequency duplicate found, start over beginning of file


print "Frequency " + str(frequency) + " has been seen twice now"
