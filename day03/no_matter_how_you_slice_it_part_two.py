#!/usr/bin/python


# Format of a claim:
# 
# #ID @ X,Y WxH
#
def parse_claim(claim):
    split_input = claim.split()
    claim_id = split_input[0].split('#')[1]
    x =  split_input[2].split(',')[0]
    y =  split_input[2].split(',')[1].split(':')[0]
    w =  split_input[3].split('x')[0]
    h =  split_input[3].split('x')[1]
    return [int(claim_id), int(x), int(y), int(w), int(h)]


def mark_fabric(claim_id, x, y, width, height):
    claim_overlaps = False
    for i in range(x, x+width):
        for j in range(y, y+height):
            if not fabric[i][j]:
                fabric[i][j].append(claim_id)
            else:
                claim_overlaps = True
                for claim_id in fabric[i][j]:
                    if claim_id in ids_with_no_overlap: ids_with_no_overlap.remove(claim_id)

    if claim_overlaps is False:
        ids_with_no_overlap.append(claim_id)


fabric = [[ [] for x in range(1000) ] for y in range(1000)]
ids_with_no_overlap = []

claim_logs = open('input.txt', 'r')

for claim in claim_logs:
    parse_claim(claim)
    claim_id, x, y, width, height = parse_claim(claim)
    #print "["+str(x)+","+str(y)+"]: " + str(width) + "x" + str(height)
    mark_fabric(claim_id, x, y, width, height)

claim_logs.close()

for claim_id in ids_with_no_overlap:
    print str(claim_id) + " has no overlap with other ids."


