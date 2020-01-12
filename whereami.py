with open('whereami.in', 'r') as fin:
    N = int(fin.readline())
    colors = fin.readline()
sol = 0
for k in range(1, N + 1):
    seen = []
    valid = True
    for start in range(N - (k - 1)):
        seg = colors[start: start + k]
        if seg not in seen:
            seen.append(seg)
        else:
            valid = False
            break
    if(valid):
        sol = k
        break

with open('whereami.out', 'w') as fout:
    fout.write(str(sol) + '\n')