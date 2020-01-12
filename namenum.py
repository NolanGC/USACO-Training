"""
ID: nolangc1
LANG: PYTHON3
PROG: namenum
"""


fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w+')


def toNum(c):
    if ord(c) < ord('Q'):
        return str((ord(c)-65)//3 + 2)
    else:
        return str((ord(c)-66)//3 + 2)


table = [[''],[''], ['A', 'B', 'C'], ['D', 'E', 'F'],['G', 'H', 'I'],['J', 'K', 'L'],['M', 'N', 'O'],['P', 'R', 'S'],
['T', 'U', 'V'],['W', 'X', 'Y']]

serial = [int(c) for c in fin.read() if c != '\n' and c != ' ']
possible_names = []
valid_names = []
with open('dict.txt','r') as fin:
    names = fin.read().split('\n')

serials = [''.join(list(map(toNum, name))) for name in names]
with open('namenum.in','r') as fin:
    serial = fin.read()[:-1]
indices = [i for i, x in enumerate(serials) if x == serial]
if(len(indices) > 0):
    for index in indices:
        fout.write(names[index] + '\n')
else:
    fout.write("NONE\n")