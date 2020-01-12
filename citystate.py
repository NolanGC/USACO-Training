with open('citystate.in', 'r') as fin:
    N = int(fin.readline())
    cities = []
    for i in range(N):
        l = fin.readline().strip().split(' ')
        cities.append([l[0][:2], l[1]])
count = 0


def bin(cities, l, r, key):
    while(l <= r):
        mid = (r + l) // 2

        if(cities[mid][0] == key):
            return mid
        elif cities[mid][0] < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1


cities.sort()
pairs = []
for city in cities:
    i = bin(cities, 0, len(cities) - 1, city[1])
    if(i != -1):
        if(city[0] == cities[i][1]):
            p = [city, cities[i]]
            # if(p not in pairs and p[::-1] not in pairs):
            pairs.append(p)


with open('citystate.out', 'w') as fout:
    fout.write(str(len(pairs)) + '\n')
