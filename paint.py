#10 minutes bih


with open('paint.in', 'r') as fin:
    first = list(map(int, fin.readline().split(' ')))
    a = first[0]
    b = first[1]
    second = list(map(int, fin.readline().split(' ')))
    c = second[0]
    d = second[1]
with open('paint.out', 'w') as fout:
    t = [i for i in range(a, b+1)]
    for i in range(c, d + 1):
        t.append(i)
    l = len(t)
    t = list(set(t))
    if(l > len(t)):
        fout.write(str(len(t) - 1))
    else:
        fout.write(str(len(t) - 2))