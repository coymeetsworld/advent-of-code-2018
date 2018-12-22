#!/usr/bin/python

# Example of step input:
# Step C must be finished before step A can begin
def parse_step(step):
    words = step.split()
    return words[1], words[7]

def print_timeline(current_second, processing_nodes, completed_nodes):
    p_nodes = ''
    for node in processing_nodes:
        #print p_nodes
        #print node
        p_nodes += node['node'] + str(node['total_secs']) + '/' + str(node['needed_secs']) + " " 
    print str(current_second) + " " + p_nodes + " " + completed_nodes
        #print "second " + str(total_seconds)
        #print processing_nodes

# Just checks if any node is ready to be processed.
def node_is_ready(queued_nodes, pre_reqs, completed_nodes):
#    print "Calling node_is_ready()"
#    print "queued_nodes " + str(queued_nodes)
#    print "pre_reqs " + str(pre_reqs)
#    print "completed_nodes " + completed_nodes
    while queued_nodes:
        #print "Completed nodes: " + completed_nodes
        queued_nodes = sorted(queued_nodes)
        for i in range(len(queued_nodes)):
            #print str(queued_nodes[i]) + " -> " + str(pre_reqs[queued_nodes[i]])
            all_prereqs_met = True
            for node in pre_reqs[queued_nodes[i]]:
                #print "Node " + node
                if node not in completed_nodes:
                    #print "Not here"
                    all_prereqs_met = False
                    break
            if all_prereqs_met:
#                print "Found a ready node"
                return True
#        print "No ready nodes"
        return False

def get_node(queued_nodes, pre_reqs, completed_nodes):
#    print "Calling get_node()"
    while queued_nodes:
        queued_nodes = sorted(queued_nodes)
        for i in range(len(queued_nodes)):
            all_prereqs_met = True
            for node in pre_reqs[queued_nodes[i]]:
                if node not in completed_nodes:
                    all_prereqs_met = False
                    break
            if all_prereqs_met:
                next_node = queued_nodes.pop(i)
#                print "Next node to be queued: " + next_node
                if next_node in graph_order:
                    queued_nodes += graph_order[next_node]
                    queued_nodes = list(set(queued_nodes)) # remove duplicates
                return next_node, queued_nodes


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


queued_nodes = graph_order[head_node]

processing_nodes = [{ 'node': head_node, 'total_secs': 0, 'needed_secs': 60+ord(head_node)-64} ]
#processing_nodes = [{ 'node': head_node, 'total_secs': 0, 'needed_secs': ord(head_node)-64} ]
busy_workers = 1
total_workers = 5
total_seconds = 0
completed_nodes = ''
print "pre_reqs:"
print pre_reqs
while queued_nodes:
    print "Currently queued_nodes:"
    print queued_nodes
    while busy_workers < total_workers and node_is_ready(queued_nodes, pre_reqs, completed_nodes):
        busy_workers +=1
        process_node, queued_nodes = get_node(queued_nodes, pre_reqs, completed_nodes)
        #print "total time: for " + process_node + ": " +str(60+ord(process_node)-64)
        processing_nodes.append({ 'node': process_node, 'total_secs': 0, 'needed_secs': 60+ord(process_node)-64})
        #processing_nodes.append({ 'node': process_node, 'total_secs': 0, 'needed_secs': ord(process_node)-64})
    while processing_nodes:
        #print "second " + str(total_seconds)
        #print processing_nodes
        total_seconds += 1
        current_busy_workers = busy_workers
        for node in processing_nodes:
            node['total_secs'] +=1

        print_timeline(total_seconds, processing_nodes, completed_nodes)
        for node in processing_nodes:
            if node['total_secs'] == node['needed_secs']:
                completed_nodes += node['node'];
                processing_nodes.remove(node)
                busy_workers -= 1

        # just in case more than 1 complete at same time
        if current_busy_workers > busy_workers:
            break


print "Completed notes: " + completed_nodes
print "Seconds: " + str(total_seconds)
