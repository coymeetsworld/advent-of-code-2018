#!/usr/bin/python


# Format of a claim:
# 
# #ID @ X,Y WxH
#
def parse_claim(claim):
    split_input = claim.split()
    x = split_input[2].split(',')[0]
    y = split_input[2].split(',')[1].split(':')[0]
    w = split_input[3].split('x')[0]
    h = split_input[3].split('x')[1]
    return [int(x), int(y), int(w), int(h)]


def mark_fabric(x, y, width, height):
    for i in range(x, x+width):
        for j in range(y, y+height):
            fabric[i][j] += 1


fabric = [[0 for x in range(1000)] for y in range(1000)]

claim_logs = open('input.txt', 'r')

for claim in claim_logs:
    parse_claim(claim)
    x, y, width, height = parse_claim(claim)
    #print "["+str(x)+","+str(y)+"]: " + str(width) + "x" + str(height)
    mark_fabric(x, y, width, height)

claim_logs.close()

inches_of_fabric_claimed_by_multiple = 0
for i in range(0, 1000):
    #print 
    for j in range(0, 1000):
        #print (str(fabric[i][j]))
        if fabric[i][j] > 1: inches_of_fabric_claimed_by_multiple += 1


print str(inches_of_fabric_claimed_by_multiple) + " inches of fabric have been claimed by two or more Elves."

