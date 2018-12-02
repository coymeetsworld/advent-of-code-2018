#!/usr/bin/python

list_of_boxes = open('input.txt', 'r')

box_ids_with_two_of_same_letter = 0
box_ids_with_three_of_same_letter = 0

for box_id in list_of_boxes:
	freq = dict()
	found_two_of_same_letter = False
	found_three_of_same_letter = False

	for letter in box_id:	
		if letter in freq:	freq[letter] += 1
		else: 							freq[letter] = 1

	for letter in freq:
		if freq[letter] == 2 and not found_two_of_same_letter:
			box_ids_with_two_of_same_letter += 1
			found_two_of_same_letter = True
		if freq[letter] == 3 and not found_three_of_same_letter:
			box_ids_with_three_of_same_letter += 1
			found_three_of_same_letter = True

list_of_boxes.close()
			


print "Ids with exactly 2 of at least one letter: " + str(box_ids_with_two_of_same_letter)
print "Ids with exactly 3 of at least one letter: " + str(box_ids_with_three_of_same_letter)

print "Checksum: " + str(box_ids_with_two_of_same_letter*box_ids_with_three_of_same_letter)


