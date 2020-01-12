"""
ID: nolangc1
LANG: PYTHON3
PROG: milk
"""

with open('milk.in', 'r') as fin:
    f = fin.readline().split(' ')
    amt = int(f[0])
    farmers = int(f[1])
    orders = []
    for i in range(farmers):
        orders.append([int(x) for x in fin.readline().split(' ')])


orders = sorted(orders)
cost = 0
for order in orders:
    if(amt == 0):
        break
    elif(amt >= order[1]):
        cost += order[0] * order[1]
        amt -= order[1]
    elif(amt < order[1]):
        cost += amt * order[0]
        amt = 0
with open('milk.out', 'w') as fout:
    fout.write(str(cost) + '\n')
