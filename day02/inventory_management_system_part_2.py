#!/usr/bin/python

list_of_boxes = open('input.txt', 'r')

box_ids_with_two_of_same_letter = 0
box_ids_with_three_of_same_letter = 0

box_ids = []

for box_id in list_of_boxes:
	box_ids.append(box_id)

list_of_boxes.close()

for i in range(len(box_ids)):
	for j in range(i+1, len(box_ids)):
		differences = 0
		#print "i: " + str(i) + " j: " + str(j)
		# assumes both ids are same length
		for c_index in range(0, len(box_ids[i])):
			if box_ids[i][c_index] != box_ids[j][c_index]:
				differences += 1
		if differences == 1:
			print box_ids[i] + " and " + box_ids[j] + " have only one difference in characters."

			



