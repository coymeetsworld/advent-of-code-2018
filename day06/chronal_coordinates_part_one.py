#!/usr/bin/python
import sys


def print_grid(grid):
	print "#######GRID########"
	for y in range(len(grid)):
		for x in range(len(grid)):
			print grid[x][y],
		print
	print "###################"
	print


def get_closest_ambiguous_coordinate(ambiguous_coordinate_list, x, y):	
	id_of_closest_ambig_coordinate = -1
	closest_distance = sys.maxint
	two_closest_ambig_coordinates = False
	for coordinates in ambiguous_coordinate_list:
		distance = abs(x - coordinates['x']) + abs(y - coordinates['y'])
		if distance < closest_distance:
			closest_distance = distance
			id_of_closest_ambig_coordinate = coordinates['id']
			two_closest_ambig_coordinates = False
		elif distance == closest_distance:
			two_closest_ambig_coordinates = True
			
	if two_closest_ambig_coordinates:
		return '.'	
	return id_of_closest_ambig_coordinate
		
		# calculate distance between x, y and coord x,y



coordinate_list = open('testinput.txt', 'r')


# abs |x2 - x1 | + |y2 -y1|
#sqrt((xa-xb)^2 + (yx-yb)^2)

max_x_or_y = 0

ambiguous_coordinate_list = []

coord_id = 1
for coordinates in coordinate_list:
	x, y = [int(c) for c in coordinates.split(',')]

	if x > max_x_or_y: max_x_or_y = x
	if y > max_x_or_y: max_x_or_y = y
	ambiguous_coordinate_list.append({'id': coord_id, 'x': x, 'y': y})
	coord_id += 1

coordinate_list.close()

print "Max len: " + str(max_x_or_y)

grid = [[0 for x in range(max_x_or_y+1)] for y in range(max_x_or_y+1)]
print_grid(grid)

for coordinates in ambiguous_coordinate_list:
	grid[coordinates['x']][coordinates['y']] = coordinates['id']

print_grid(grid)

# For each grid section, calculate closest ambigulous_coordinate and mark it
for x in range(len(grid)):
	for y in range(len(grid)):
		grid[x][y] = get_closest_ambiguous_coordinate(ambiguous_coordinate_list, x, y)	


print_grid(grid)

#TODO find finate_locations and largest one


