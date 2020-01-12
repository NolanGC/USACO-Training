
with open('moobuzz.in', 'r') as fin:
    N = int(fin.readline())

last_num = 0
cur = 0
count = 0

while(count < N):
    if(cur % 3 != 0 and cur % 5 != 0 and cur % 15 != 0):
        count += 1 
        last_num = cur
    cur += 1

with open('moobuzz.out', 'w') as fout:
    fout.write(str(last_num) + '\n')
