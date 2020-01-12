import itertools
def isConsistent(pair, sessions):
    a = pair[0]
    b = pair[1]
    awon = 0
    bwon = 0
    for session in sessions:
        if(session.index(a) < session.index(b)):
            awon += 1
        else:
            bwon += 1
    return (awon == len(sessions) or bwon == len(sessions))
        
with open('gymnastics.in', 'r') as fin:
    K, N = list(map(int, fin.readline().split(' ')))
    sessions = []
    for i in range(K):
        sessions.append(list(map(int, fin.readline().split(' '))))

pairs = list(itertools.combinations(range(1,N+1), 2))
count = 0
for pair in pairs:
    if(isConsistent(pair, sessions)):
        count += 1

with open('gymnastics.out', 'w') as fout:
    fout.write(str(count) + '\n')
