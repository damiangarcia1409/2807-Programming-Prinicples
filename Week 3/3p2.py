
canidates = [["Angus",0],["Betty",0],["Cathy",0]]
tieFlag = False
winThreshold = 0.0
winners = []

#Get input
canidates[0][1]=int(input("Angus votes? "))
canidates[1][1]=int(input("Betty votes? "))
canidates[2][1]=int(input("Cathy votes? "))

winThreshold = winThreshold + canidates[0][1] + canidates[1][1] + canidates[2][1]
winThreshold = winThreshold / 2

#print(winThreshold)

#print(canidates)

def comp2(p1,p2,p3):
    #if two of them are the same return all
    if p1 == p2 or p1 == p3:
        #return all
        return True
    elif p3 == p1 or p3 == p2:
        #return all
        return True

def topTwo():
    lowestArray = 0
    lowestVal = 999999
    for p in range(len(canidates)):
        #print(p)
        if canidates[p][1] < lowestVal:
            lowestArray = p
            lowestVal = canidates[p][1]

    #print("removing" + str(lowestArray))
    canidates.pop(lowestArray)
    print("next round: " + canidates[0][0] + " "+ canidates[1][0])

# if someone has over the threshold they win
if canidates[0][1] > winThreshold:
    print(canidates[0][0] + " Wins")
elif canidates[1][1] > winThreshold:
    print(canidates[1][0] + " Wins")
elif canidates[2][1] > winThreshold:
    print(canidates[2][0] + " Wins")

#if all 3 are the same print all
elif canidates[0][1] == canidates[1][1] and canidates[1][1] == canidates[2][1]:
    print("Next Round: Angus, Betty and Cathy")

#else compare them one by one with a function
elif comp2(canidates[0][1],canidates[1][1],canidates[2][1]):
    print("Next Round: Angus, Betty and Cathy")

else:
    topTwo()











