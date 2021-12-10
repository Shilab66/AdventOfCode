file = open("Day6Test.txt", "r")
list2 = file.readline().split(",")
list1 = []

for i in list2:
    list1.append(int(i))

for i in range(256):
    print(i)
    appended = 0
    for j in list1:
        if j == 0:
            appended += 1
            list1[list1.index(j)] = 6
        else:
            list1[list1.index(j)] = j-1
    for k in range(appended):
        list1.append(8)

#print(list1)

print(len(list1))
