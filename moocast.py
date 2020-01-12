from collections import defaultdict
import math


class Cow():
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ') ' + str(self.p)


def dist(u, v):
    return math.sqrt((v.x - u.x)**2 + (v.y - u.y)**2)


with open('moocast.in', 'r') as fin:
    N = int(fin.readline())
    cows = []
    for i in range(N):
        l = list(map(int, fin.readline().split(' ')))
        cows.append(Cow(l[0], l[1], l[2]))

adj = defaultdict(list)


def addEdge(adj, u, v):
    if(v not in adj[u]):
        adj[u].append(v)


for i in range(len(cows)):
    for j in range(len(cows)):
        if(i != j and dist(cows[i], cows[j]) <= cows[i].p):  # i -> j is valid
            addEdge(adj, i, j)
        if(i != j and dist(cows[i], cows[j]) <= cows[j].p):  # j -> i is valid
            addEdge(adj, j, i)


def BFS(s, adj):
    level = {s: 0}
    visited = 1  # includes s
    i = 1
    frontier = [s]  # level i-1
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    visited += 1
                    next.append(v)
        frontier = next
        i += 1
    return visited


best = 0
for i in range(len(cows)):
    c = BFS(i, adj)
    if(c > best):
        best = c


with open('moocast.out', 'w') as fout:
    fout.write(str(best) + '\n')
