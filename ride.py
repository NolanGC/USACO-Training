"""
ID: nolangc1
LANG: PYTHON3
PROG: ride
"""

def ascii_prod(values):
    prod = 1
    for v in values:
        prod *= v
    return prod


fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w+')
raw = fin.read().splitlines()

comet = raw[0]
comet_values = [ord(c) - 64 for c in comet]

group  = raw[1]
group_values = [ord(c) - 64 for c in group]

comet_prod = ascii_prod(comet_values)
group_prod = ascii_prod(group_values)

if(comet_prod % 47 == group_prod % 47):
    fout.write ("GO\n")
    fout.close()
else:
    fout.write ("STAY\n")
    fout.close()
