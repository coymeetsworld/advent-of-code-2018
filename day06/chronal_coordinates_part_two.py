#!/usr/bin/python
import math

def get_total_distance_between_all_ambiguous_coordinates(x, y, ambiguous_coordinate_list):
    total_distance = 0
    for coordinates in ambiguous_coordinate_list:
        total_distance += abs(x-coordinates['x']) + abs(y-coordinates['y'])
    return total_distance
        


#coordinate_list = open('testinput.txt', 'r')
coordinate_list = open('input.txt', 'r')

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


safe_region_size = 0

# For each grid section, calculate closest ambigulous_coordinate and mark it
for x in range(max_x_or_y+1):
    for y in range(max_x_or_y+1):
        total_distance = get_total_distance_between_all_ambiguous_coordinates(x, y, ambiguous_coordinate_list)
        #if total_distance < 32:
        if total_distance < 10000:
           safe_region_size += 1


print "Safe region size is " + str(safe_region_size)

