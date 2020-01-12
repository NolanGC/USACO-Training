"""
ID: nolangc1
LANG: PYTHON3
PROG: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w+')
r = fin.read().splitlines()

people = []
np = r[0] 
for i in range(int(np)):
    people.append((r[i + 1], 0))
people_dict = dict(people)

i = int(np) + 1

while(i < len(r)):
    giver = r[i]
    amt = int(r[i+1].split(' ')[0])
    num_getters  = int(r[i+1].split(' ')[1])
    getters = []
    for j in range(num_getters):
        getters.append(r[i+2+j])

    if(amt == 0):
        amt_per = 0
        leftover = 0
    else:
        leftover = amt % num_getters
        amt_per = (amt - leftover) // num_getters
    people_dict[giver] = people_dict[giver] - amt + leftover
    for getter in getters:
        people_dict[getter] += amt_per
    i += (2 + num_getters)

for person in people_dict:
    fout.write(person + " " + str(people_dict[person]) + "\n")

