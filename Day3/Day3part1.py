file = open("Day3.txt", "r")
list1 = []
gammaRate = "";
EpsilonRate = "";
ones = 0
zeros = 0
splice = 5

for x in file:
    list1.append(str(x)[:12])

#print(list1)

for y in range(5):
    splice -= 1
    ones = 0
    zeros = 0
    for z in list1:
        if z[y] == "1":
            ones += 1
        else:
            zeros+=1"""
    #if ones > zeros:
    for i in list1:
        for j in range(len(list1)):
            list1[j] = i[:splice]
    print(list1)
    #else:
        

#print(gammaRate, EpsilonRate)
