#AUTHOR : Yash PACHCHIGAR
#DATE : 11/07/2021
#DESCRIPTION : Bellman ford algorithm + number of hops
#INPUT : network_graph, source, edges
#OUTPUT : dist, hops
#TIME COMPLEXITY : O(V*E)
#SPACE COMPLEXITY : O(V)

# Create a netowrk graph
network_graph = [
    ('u', 'x',{'weight': 1}), 
    ('u', 'w', {'weight':7}), 
    ('v' ,'x', {'weight':1}), 
    ('v' , 'w', {'weight':1}), 
    ('x', 'w', {'weight':4}), 
    ('x', 'y', {'weight':2}), 
    ('y', 'z', {'weight':3}), 
    ('y', 'w', {'weight':5}), 
    ('z', 'w', {'weight':6})]

#Define soruce of the graph
source = 'u'
#Create a list of edges
edges = [(routers, targets, attr['weight']) for routers, targets, attr in network_graph]


#funciton to calculate the shortest path using bellman ford algorithm + number of hops
def ypachchi_bellman(network_graph, source, edges):
    dist = {source: 0}
    hops = {source: 0}
    for i in range(len(network_graph) - 1):
        for u, v, w in edges:
            if dist.get(u, float('inf')) + w < dist.get(v, float('inf')):
                dist[v] = dist[u] + w
                hops[v] = hops[u] + 1
    return dist , hops

#print shortest path from source for all sources
shortest_path_dict = ypachchi_bellman(network_graph, source, edges)
print("Source is '{}'".format(source))
print("\n")
print ("Target"+" "+"Distance"+" "+"Hops")

#print it out in a table
for i in shortest_path_dict[0].keys():
    print(i, "      ", shortest_path_dict[0][i], "      ", shortest_path_dict[1][i])