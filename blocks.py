import itertools

with open('blocks.in', 'r') as fin:
    N = int(fin.readline())
    cards = []
    for i in range(N):
        cards.append(fin.readline().rstrip().split(' '))

alpha = [0 for i in range(26)]

for i in range(2**N):
    i = str(bin(i))[2:]
    dif = len(i) - N
    if dif > 0:
        for q in range(dif):
            i = '0' + i
    i = [int(c) for c in i]
    combo = ''
    for j in range(len(i)):
        combo += cards[j][i[j]]
    for c in combo:
        if(alpha[ord(c) - 97] < combo.count(c)):
            alpha[ord(c) - 97] = combo.count(c)

with open('blocks.out', 'w') as fout:
    for i in alpha:
        fout.write(str(i) + '\n')
