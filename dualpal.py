"""
ID: nolangc1
LANG: PYTHON3
PROG: dualpal
"""
import string
digs = string.digits + string.ascii_uppercase
def baseX(x, base):
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    digits.reverse()
    return ''.join(digits)

def isPalindrome(N):
    return [c for c in str(N)] == [c for c in str(N)][::-1]

with open('dualpal.in', 'r') as fin:
    t = fin.readline().split(' ')
    N = int(t[0])
    S = int(t[1])

curr = S + 1
out = ''
while(N > 0):
    count = 0
    for i in range(2, 11):
        if(isPalindrome(baseX(curr, i))):
            count += 1
    if(count >= 2):
        out += str(curr) + '\n'
        N-=1
    count = 0
    curr += 1
with open('dualpal.out', 'w') as fout:
    fout.write(out)