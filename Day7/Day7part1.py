file = open("Day7.txt", "r");
list2 = file.readline().split(",")
list1 = []
maximum = 0
minimum = 0
least = 999999999999

for i in list2:
  list1.append(int(i))

maximum = max(list1)
minimum = min(list1)

print(minimum, maximum)

for i in range(minimum, maximum+1):
  fuel = 0
  for j in list1:
    for k in range(1, abs(j-i)+1):
        fuel+=k
  if fuel < least:
      least = fuel
  print(i)

print(least)
