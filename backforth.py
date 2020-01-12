with open('backforth.in', 'r') as fin:
    f = fin.readlines()
    buckets1 = list(set(map(int, f[0].split(' '))))
    buckets2 = list(set(map(int, f[1].split(' '))))

b1 = [buckets1, [], [], [], []]
b2 = [buckets2, [], [], [], []]
tank1 = [1000, [], [], [], []]
tank2 = [1000, [], [], [], []]
print(b1, b2)
#tuesday
for i in buckets1:
    tank1[1].append(tank1[0] - i)
    b2[1].append(buckets1)
#wednesday
