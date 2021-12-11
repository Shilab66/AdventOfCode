file = open("Day8.txt", "r")
list1 = []
count = 0

for i in file:
  lineList = i.split(" | ")
  output = lineList[1]
  list1.append(output.split(" "))

for i in list1:
    last = i[-1]
    i[-1] = last[:-1]


for i in list1:
    for j in i:
        if (len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7):
            #print(j, len(j))
            count += 1

print(count)
