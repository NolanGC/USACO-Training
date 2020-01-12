"""
ID: nolangc1
LANG: PYTHON3
PROG: palsquare
"""
import string
digs = string.digits + string.ascii_uppercase

def int2base(x, base):
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    digits.reverse()
    return ''.join(digits)
def isPalindrome(N):
    return [c for c in str(N)] == [c for c in str(N)][::-1]

fin = open('palsquare.in', 'r')


B = int(fin.read())
print(B)
out = ''
for N in range(1, 301):
    if(isPalindrome(int2base(N**2, B))):
        out += str(int2base(N, B)) + ' ' + str(int2base(N**2, B)) + '\n'
with open('palsquare.out', 'w+') as fout:
    fout.write(out)