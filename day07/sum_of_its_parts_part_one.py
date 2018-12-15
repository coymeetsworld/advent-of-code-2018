#!/usr/bin/python

# Example of step input:
# Step C must be finished before step A can begin
def parse_step(step):
    words = step.split()
    return words[1], words[7]

instructions = open('input.txt', 'r')

graph_order = {}
pre_reqs = {}

head_node = ''
for step in instructions:
    src, dst = parse_step(step)

    if head_node == '':
        head_node = src
        #print "Head node: " + src

    if src not in graph_order:
        graph_order[src] = [dst]
    else:
        graph_order[src].append(dst)

    if dst not in pre_reqs:
        pre_reqs[dst] = [src]
    else:
        pre_reqs[dst].append(src)

steps = head_node
queued_nodes = graph_order[head_node]
      
while queued_nodes:
    queued_nodes = sorted(queued_nodes)
    #print queued_nodes
    for i in range(len(queued_nodes)):
        #print str(queued_nodes[i]) + " -> " + str(pre_reqs[queued_nodes[i]])
        all_prereqs_met = True
        for node in pre_reqs[queued_nodes[i]]:
            if node not in steps:
                all_prereqs_met = False
                break
        if all_prereqs_met:
            next_node = queued_nodes.pop(i)
            break

    #print "next node to process: " + next_node

    if next_node not in steps:
        steps += next_node
        if next_node in graph_order:
            queued_nodes += graph_order[next_node]

print steps
