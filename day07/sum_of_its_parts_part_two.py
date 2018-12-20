#!/usr/bin/python

# Example of step input:
# Step C must be finished before step A can begin
def parse_step(step):
    words = step.split()
    return words[1], words[7]

def node_is_ready(completed_nodes, pre_reqs, queued_nodes):
    while queued_nodes:
        queued_nodes = sorted(queued_nodes)
        #print queued_nodes
        for i in range(len(queued_nodes)):
            #print str(queued_nodes[i]) + " -> " + str(pre_reqs[queued_nodes[i]])
            all_prereqs_met = True
            for node in pre_reqs[queued_nodes[i]]:
                if node not in completed_nodes:
                    all_prereqs_met = False
                    break
            if all_prereqs_met:
                return True
    return False

def get_node(queued_nodes, pre_reqs, completed_nodes):
    while queued_nodes:
        queued_nodes = sorted(queued_nodes)
        for i in range(len(queued_nodes)):
            all_prereqs_met = True
            for node in pre_reqs[queued_nodes[i]]:
                if node not in completed_nodes:
                    all_prereqs_met = False
                    break
            if all_prereqs_met:
                return queued_nodes.pop(i), queued_nodes


instructions = open('testinput.txt', 'r')

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


queued_nodes = graph_order[head_node]
# Heres the steps to process
# Pop out the first node
# If not all workers are busy, check to see if another node can be removed
#   continue into all workers are queued or no more nodes can be removed
#   process time, while loop for seconds
#     if a task is done, mark worker free and see if another node can be removed
#     if no more nodes are left, exit out of loop

processing_nodes = [{ 'node': head_node, 'total_secs': 0, 'needed_secs': ord(head_node)-64} ]
busy_workers = 1
total_workers = 2
total_seconds = 0
completed_nodes = ''

while queued_nodes:
    while busy_workers < total_workers and node_is_ready(queued_nodes, pre_reqs, completed_nodes):
        busy_workers +=1
        process_node, queued_nodes = get_node(queued_nodes, pre_reqs, completed_nodes)
        processing_nodes.append({ 'node': process_node, 'total_secs': 0, 'needed_secs': ord(process_node)-64})
    while True:
        total_seconds += 1
        current_busy_workers = busy_workers
        for node in processing_nodes:
            node['total_secs'] +=1
            if node['total_secs'] == node['needed_secs']:
                completed_nodes += node['node'];
                processing_nodes.remove(node)
                busy_workers -= 1

        # just in case more than 1 complete at same time
        if current_busy_workers > busy_workers:
            break


