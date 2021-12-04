file = open("Day3.txt", "r")
list1 = []
list2 = []
list3 = []
list4 = []
ones = 0
zeros = 0
most = 0
least = 0

for x in file:
    list1.append(str(x)[:12])
    list3.append(str(x)[:12])

for i in range(12):
    ones = 0
    zeros = 0
    for z in list1:
        if z[i] == "1":
            ones += 1
        else:
            zeros+=1
    if ones > zeros:
        most = 1
    elif zeros > ones:
        most = 0
    else:
        most = 1
    
    for j in list1:
        if j[i] == str(most):
            list2.append(j)   
    
    list1=list2
    list2=[] 
        

    if(len(list1) == 1):
        print("WHOOOOOO")
        print(str(list1))
        break
    




for k in range(12):
    ones = 0
    zeros = 0
    for z in list3:
        if z[k] == "1":
            ones += 1
        else:
            zeros+=1
    if ones < zeros:
        least = 1
    elif zeros < ones:
        least = 0
    else:
        least = 0
    
    for j in list3:
        if j[k] == str(least):
            list4.append(j)
    
    
    list3=list4
    list4=[]     

    if(len(list3) == 1):
        print("WHOOOOOO")
        print(str(list3))
        break       
