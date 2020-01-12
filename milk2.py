"""
ID: nolangc1
LANG: PYTHON3
PROG: milk2
"""


fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w+')

r = set()

N = int(fin.readline())
for i in range(N):
    s, e = map(int, fin.readline().split())
    r.update(range(s,e))

l = [int(i in r) for i in range(min(r), max(r) + 1)]
s = ''.join(list(map(str, l)))

fout.write(str(len(max(s.split('0'), key = len))) + ' ' + str(len(max(s.split('1'), key = len))) +'\n')
