with open('cowtip.in', 'r') as fin:
    N = int(fin.readline())
    cows = []
    for i in range(N):
        cows.append([int(c) for c in fin.readline() if c != '\n'])

def tip(matrix):
    bottom = matrix(len(matrix)-1)
    for i in range(len(bottom) - 1, -1, -1):
        if(bottom[i] == 1):
            tip()


    