cows = []
totalW = 0
stoppedW = 0
with open('meetings.in', 'r') as fin:
    N, L = list(map(int, fin.readline().split(' ')))
    for i in range(N):
        l = list(map(int, fin.readline().split(' ')))
        cows.append(l)
        totalW += l[0]

T = 0
print(T, cows)
meetings = 0
while(stoppedW < totalW // 2):

    #second passes, all cows move by their velocity
    for cow in cows:
        cow[1] += (cow[2] * 0.5)
        #reached barn
        if(cow[1] == 0 or cow[1] == L):
            #stop cow
            stoppedW += cow[0] 
            cows.remove(cow)
            print("cow stopped, stopped weight is now ", stoppedW, "/", totalW//2)  
    T += 0.5

    print(T, cows)

    #cows.sort(key = lambda x: x[1])
    for cow in cows:
        for otherCow in cows:
            #meeting
            if(cow[1] == otherCow[1]):
                print("meeting at ", T, " on ", cow[1])
                temp = cow[2]
                cow[2] = otherCow[2]
                otherCow[2] = temp
                meetings += 1
            
print(meetings)


# if(cows[i][1] - cows[i + 1][1] == 0):
            #print("meeting at ",cows[i][1], T)
            #temp = cows[i][2]
            #cows[i][2] = cows[i + 1][2]
            #cows[i + 1][2] = temp
            #meetings += 1