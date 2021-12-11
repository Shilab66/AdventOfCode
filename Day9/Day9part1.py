file = open("Day9.txt", "r")
list1 = []
iIndex = 0
jIndex = 0
lowPoints = []
riskLevel = []
count = 0

for i in file:
    if "\n" in i:
        list1.append(i[:-1])
    else:
        list1.append(i)


for i in list1:
    jIndex = 0
    for j in i:

        if (iIndex != 0 and iIndex != 99 and jIndex != 0 and jIndex != 99):
            previous = i[jIndex-1]
            after = i[jIndex+1]
            belowLine = list1[iIndex+1]
            below = belowLine[jIndex]
            aboveLine = list1[iIndex-1]
            above = aboveLine[jIndex]
            if (j < previous and j < after and j<above and j<below):
                lowPoints.append(j)
                riskLevel.append(int(j)+1)

        elif(iIndex == 0 and jIndex != 0 and jIndex != 99):
            previous = i[jIndex-1]
            after = i[jIndex+1]
            belowLine = list1[iIndex+1]
            below = belowLine[jIndex]
            aboveLine = list1[iIndex-1]
            if (j < previous and j < after and j<below):
                lowPoints.append(j)
                riskLevel.append(int(j)+1)
        
        elif(iIndex == 99 and jIndex != 0 and jIndex != 99):
            previous = i[jIndex-1]
            after = i[jIndex+1]
            aboveLine = list1[iIndex-1]
            above = aboveLine[jIndex]
            if (j < previous and j < after and j<above):
                lowPoints.append(j)
                riskLevel.append(int(j)+1)
        
        elif(jIndex == 0 and iIndex != 0 and iIndex != 99):
            after = i[jIndex+1]
            belowLine = list1[iIndex+1]
            below = belowLine[jIndex]
            aboveLine = list1[iIndex-1]
            above = aboveLine[jIndex]
            if (j < after and j<above and j<below):
                lowPoints.append(j)
                riskLevel.append(int(j)+1)
        
        elif(jIndex == 99 and iIndex != 0 and iIndex != 99):    
            previous = i[jIndex-1]
            belowLine = list1[iIndex+1]
            below = belowLine[jIndex]
            aboveLine = list1[iIndex-1]
            above = aboveLine[jIndex]
            if (j < previous and j<above and j<below):
                lowPoints.append(j)
                riskLevel.append(int(j)+1)
        
        jIndex += 1
    iIndex += 1
        
print(riskLevel)

for i in riskLevel:
    count += i
print(count)
