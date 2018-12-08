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

def find_infinite_locations(grid):
        inf_locations = []
        for x in range(len(grid)):
            if grid[x][0] not in inf_locations:
                inf_locations.append(grid[x][0])
        for x in range(len(grid)):
            if grid[x][len(grid)-1] not in inf_locations:
                inf_locations.append(grid[x][len(grid)-1])
            
        for y in range(len(grid)):
            if grid[0][y] not in inf_locations:
                inf_locations.append(grid[0][y])
        for y in range(len(grid)):
            if grid[len(grid)-1][y] not in inf_locations:
                inf_locations.append(grid[len(grid)-1][y])

        return inf_locations

def get_largest_contained_area(infinite_locations, grid):
    contained_areas = {}
    for y in range(len(grid)):
	for x in range(len(grid)):
            if grid[x][y] not in infinite_locations:
                if grid[x][y] not in contained_areas:
                    contained_areas[grid[x][y]] = 1
                else:
                    contained_areas[grid[x][y]] += 1
    print contained_areas
    max_size = -1
    for contained_area, size in contained_areas.items():
        if size > max_size:
            max_size = size
            
    return max_size


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



coordinate_list = open('input.txt', 'r')


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

infinite_locations = find_infinite_locations(grid)
print infinite_locations

largest_contained_area =  get_largest_contained_area(infinite_locations, grid)

print "Largest contained area size is " + str(largest_contained_area)
#TODO find finate_locations and largest one


