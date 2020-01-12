with open('lifeguards.in', 'r') as fin:
    N = int(fin.readline())
    guards = []
    for i in range(N):
        guards.append(list(map(int, fin.readline().split(' '))))

lastTime = max(guards, key=lambda x: x[1])[1]

times = [0 for i in range(lastTime)]
for guard in guards:
    for t in range(guard[0], guard[1]):
        times[t] += 1

timeCovered = len(times) - times.count(0)

minTimesOpened = 1001
for guard in guards:
    timesOpened = 0
    for t in range(guard[0], guard[1]):
        if(times[t] - 1 == 0):
            timesOpened += 1
    if(timesOpened < minTimesOpened):
        minTimesOpened = timesOpened

with open('lifeguards.out', 'w') as fout:
    fout.write(str(timeCovered - minTimesOpened) + '\n')