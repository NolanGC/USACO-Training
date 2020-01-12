import itertools
cows = {
    'Bessie' : '1',
    'Buttercup' : '2',
    'Belinda' : '3',
    'Beatrice' : '4',
    'Bella' : '5',
    'Blue' : '6',
    'Betsy' : '7',
    'Sue' : '8'
}
cows2 = {
    '1':'Bessie',
    '2':'Buttercup',
    '3':'Belinda',
    '4':'Beatrice',
    '5':'Bella',
    '6':'Blue',
    '7':'Betsy',
    '8': 'Sue'
}
with open('lineup.in', 'r') as fin:
    N = int(fin.readline())
    rules = []
    for i in range(N):
        txt = fin.readline().rstrip("\n\r").split(' must be milked beside ')
        rules.append([cows[txt[0]], cows[txt[1]]])
def isValid(lineup, rules):
    for rule in rules:
        if(abs(lineup.index(rule[0]) - lineup.index(rule[1])) != 1):
            return False
    return True

def listToString(s):  
    str1 = "" 
    return (str1.join(s)) 

lst = ['1', '2', '3', '4', '5', '6', '7', '8']
lineups = itertools.permutations(lst)
print(lineups)
bestValid = ['8','8','8','8','8','8','8','8']
for lineup in lineups:
    if(isValid(lineup, rules)):
        list1 = [cows2[i] for i in lineup]
        list2 = [cows2[i] for i in bestValid]
        if(listToString(list1) < listToString(list2)):
            bestValid = lineup
sol = ''
for k in bestValid:
    sol += cows2[k] +'\n'
with open('lineup.out', 'w') as fout:
    fout.write(sol)
