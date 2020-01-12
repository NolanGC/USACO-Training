"""
ID: nolangc1
LANG: PYTHON3
PROG: transform
"""


def rot90(p):
    if(len(p) == 1):
        return p
    else:
        return list(zip(*p[::-1]))

def rot180(p):
    if(len(p) == 1):
        return p
    else:
        first = list(zip(*p[::-1]))
        return list(zip(*first[::-1]))
def rot270(p):
    if(len(p) == 1):
        return p
    else:
        first = list(zip(*p[::-1]))
        second = list(zip(*first[::-1]))
        return list(zip(*second[::-1]))
def reflect(p):
    return [tuple(row[::-1]) for row in p]

def solve(p, q):
    if(rot90(p) == q):
        return '1\n'
    elif(rot180(p) == q):
        return '2\n'
    elif(rot270(p) == q):
        return '3\n'
    elif(reflect(p) == q):
        return '4\n'
    elif(rot90(reflect(p)) == q or rot180(reflect(p)) == q or rot270(reflect(p)) == q):
        return '5\n'
    elif(p == q):
        return '6\n'
    else:
        return '7\n'

fin = open('transform.in', 'r')
fout = open('transform.out', 'w+')
N = int(fin.readline())

p = [[c for c in fin.readline() if c != '\n'] for i in range(N)]
q = [[c for c in fin.readline() if c != '\n'] for i in range(N)]


fout.write(solve(p,[tuple(r) for r in q]))