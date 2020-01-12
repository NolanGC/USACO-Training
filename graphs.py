from collections import defaultdict
def BFS(s, adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s] #level i-1
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
parent = {s: None}
def DFS_Visit(V, adj, s):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_Visit(V, adj, v)
def DFS(V, adj):
    parent={}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_Visit(V, adj, s)


graph = defaultdict(list)


