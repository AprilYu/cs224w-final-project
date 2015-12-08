import snap
import math

# q_values = {}
# highest_q_value = []
# a_values = {}
# final_overall_q = []

graph = snap.LoadEdgeList(snap.PUNGraph, 'user_edges_one_day_no_self.csv', 1, 2, ',')

print "made graph"

# numEdges = 0
# with open("karate.txt") as f:
# 	for line in f:
# 		numEdges += 1

# for node in graph.Nodes():

# 	a_values[node.GetId()] = float(node.GetOutDeg()) / (2 * numEdges)

# 	for neighbor in node.GetOutEdges():
# 		val = 1/float(numEdges) - (node.GetOutDeg()*snap.GetNI(neighbor).GetOutDeg())/math.pow(2*numEdges, 2)
# 		if node.GetId() in q_values:
# 			q_values[node.GetId()].append((val, node.GetId(), neighbor))
# 		else:
# 			q_values[node.GetId()] = [(val, node.GetId(), neighbor)]

# 		if neighbor in q_values:
# 			q_values[neighbor].append((val, neighbor, node.GetId()))
# 		else:
# 			q_values[neighbor] = [(val, neighbor, node.GetId())]

# while(True):
# 	highest_q_value = []
# 	for k,v in q_values:
# 		highest_q_value.append(max(v))
# 	largest_q = max(highest_q_value)

########## Clauset et Al algorithm ##########
# CmtyV = snap.TCnComV()
# modularity = snap.CommunityCNM(graph, CmtyV)
# for Cmty in CmtyV:
# 	print "Community: "
# 	for NI in Cmty:
# 		print NI
# print"The modularity of the network is %f" % modularity

########## Girvan-Newman Community Detection ##########
CmtyV = snap.TCnComV()
modularity = snap.CommunityGirvanNewman(graph, CmtyV)
for Cmty in CmtyV:
	print "Community: "
	for NI in Cmty:
		print NI
print "The modularity of the network is %f" % modularity