#USACO 2016 DECEMBER BRONZE P1 -- DONE IN 12 MINUTES


with open('square.in', 'r') as fin:
    r1 = list(map(int, fin.readline().split(' ')))
    r2 = list(map(int, fin.readline().split(' ')))

with open('square.out', 'w') as fout:
    length = max(r2[2],r1[2]) - min(r1[0], r2[0])
    width = max(r1[3],r2[3]) - min(r1[1], r2[1])
    fout.write(str(max(length,width)**2))