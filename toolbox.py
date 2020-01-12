from collections import defaultdict 

#Binary Search
def bs(data, target):
    low = 0
    high = len(data) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(target == data[mid]):
            return mid
        elif(target < data[mid]):
            high = mid - 1
        elif(target > data[mid]):
            low = mid +  1
    return False

#Rotate Matrix
def rot90(p):
    if(len(p) == 1):
        return p
    else:
        return list(zip(*p[::-1]))

#Display 2D Array
def display2D(m):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))


graph = defaultdict(list) 
def addEdge(graph,u,v): 
    graph[u].append(v) 
def generate_edges(graph): 
    edges = [] 
    for node in graph: 
        for neighbour in graph[node]: 
            edges.append((node, neighbour)) 
    return edges 
def find_path(graph, start, end, path =[]): 
  path = path + [start] 
  if start == end: 
    return path 
  for node in graph[start]: 
    if node not in path: 
      newpath = find_path(graph, node, end, path) 
      if newpath:  
        return newpath 
      return None
addEdge(graph, 1,2)
addEdge(graph, 1,5)
addEdge(graph, 5,8)

print(find_path(graph, 1, 5))