
with open('outofplace.in', 'r') as fin:
    N = int(fin.readline())
    arr = []
    for i in range(N):
        arr.append(int(fin.readline()))

arrpos = [*enumerate(arr)]
arrpos.sort(key = lambda x: x[1])
vis = {k:False for k in range(N)} 

total = 0
for i in range(N):
    if(vis[i] or arrpos[i][0] == i):
        continue
    cycle_size = 0
    j = i
    while not vis[j]:
        vis[j] = True
        j = arrpos[j][0]
        cycle_size += 1
    if(cycle_size > 0):
        total += (cycle_size - 1)

with open('outofplace.out', 'w') as fout:
    fout.write(str(total -1) + '\n')
