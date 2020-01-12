"""
ID: nolangc1
LANG: PYTHON3
PROG: friday
"""

def leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
def next_day(d):
    if(d == 7):
        return 1
    else:
        return d + 1

fin = open('friday.in', 'r')
fout = open('friday.out', 'w+')

n = int(fin.read())
freqs = dict([(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)])
months = []
for m in range(1, 13):
    thirty = [9, 4, 6, 11]
    if(m in thirty):
        months.append((m, 30))
    else:
        months.append((m, 31))
m_days = dict(months)


day_of_week = 3
for y in range(1900, 1900 + n):
    if(leap_year(y)):
        m_days[2] = 29
    else:
        m_days[2] = 28

    for m in range(1, 13):
        for d in range(1, m_days[m] + 1):
            if(d == 13):
                freqs[day_of_week] += 1
            day_of_week = next_day(day_of_week)  

for f in range(len(list(freqs.values()))):
    if(f == len(list(freqs.values())) - 1):
        fout.write(str(list(freqs.values())[f]))
    else:
        fout.write(str(list(freqs.values())[f]) + ' ')
fout.write('\n')
fout.close()
