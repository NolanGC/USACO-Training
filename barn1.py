"""
ID: nolangc1
LANG: PYTHON3
PROG: barn1
"""

with open('barn1.in', 'r') as fin:
    boards, stalls, numcows = map(int, fin.readline().split())

    cows = [int(x) for x in fin.readlines()]
    cows.sort()

if(boards >= numcows):
    sol = numcows
else:
    gaps = [(cows[i+1] - cows[i] - 1) for i in range(numcows-1)]
    gaps.sort()

    maxgaps = 0 
    for i in range(boards-1):
        maxgaps += gaps.pop()
    sol = max(cows) - min(cows) + 1 - maxgaps
with open('barn1.out', 'w') as fout:
    fout.write(str(sol) +'\n')
    