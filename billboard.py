import math

with open('billboard.in', 'r') as fin:
    b1 = list(map(int, fin.readline().split(' ')))
    b2 = list(map(int, fin.readline().split(' ')))
    t = list(map(int, fin.readline().split(' ')))

total = (b1[2] - b1[0]) * (b1[3] - b1[1]) + (b2[2] - b2[0]) * (b2[3] - b2[1])
b1_cov = 0
b2_cov = 0

#iter over all values covered by truck
for y in range(t[3], t[1] - 1, - 1):
    for x in range(t[0], t[2] + 1):
        #if covered, subtract from total
        if(x >= b1[0] and x <= b1[2] and y >= b1[1] and y <= b1[3]):
            b1_cov += 1
        elif(x >= b2[0] and x <= b2[2] and y >= b2[1] and y <= b2[3]):
            b2_cov += 1

total -= (math.sqrt(b1_cov) - 1) ** 2
total -= (math.sqrt(b2_cov) - 1) ** 2
total = int(total)
with open('billboard.out', 'w') as fout:
    fout.write(str(total) + '\n')
