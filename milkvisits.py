from collections import defaultdict 

graph = defaultdict(list) 
def addEdge(graph,u,v): 
    graph[u].append(v) 
def generate_edges(graph): 
    edges = [] 
    for node in graph: 
        for neighbour in graph[node]: 
            edges.append((node, neighbour)) 
    return edges 

def find_all_paths(graph, src, dest, path =[]): 
  path = path + [src] 
  if src == dest: 
    return [path] 
  paths = [] 
  for node in graph[src]: 
    if node not in path: 
      newpaths = find_all_paths(graph, node, dest, path) 
    for newpath in newpaths: 
      paths.append(newpath) 
  return paths

with open('milkvisits.in', 'r') as fin:
    num_farms, num_friends = list(map(int, fin.readline().split(' ')))
    breeds = [c for c in fin.readline()]
    for i in range(num_farms - 1):
        source, target = list(map(int, fin.readline().split(' ')))
        addEdge(graph, source, target)
    friends = []
    for i in range(num_friends):
        friends.append(fin.readline().strip().split(' '))

o = ''

breeds_dict = {}
for i in range(num_farms):
    breeds_dict[i + 1] = breeds[i]


for friend in friends:
    source = int(friend[0])
    target = int(friend[1])
    if(breeds_dict[target] == friend[2]):
        o += '1'
    else:
        paths = find_all_paths(graph, source, target)
        found_valid = False
        for path in paths:
            if(found_valid):
                break
            for node in path:
                if(breeds_dict[node] == friend[2]):
                    found_valid = True
                    o += '1'
                    break
        if(not found_valid):
            o += '0'
with open('milkvisits.out', 'w') as fout:
    fout.write(o + '\n')
