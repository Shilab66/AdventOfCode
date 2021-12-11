file = open("Day7.txt", "r");
list2 = file.readline().split(",")
list1 = []
maximum = 0
minimum = 0
least = 999999

for i in list2:
  list1.append(int(i))
print(list1)

maximum = max(list1)
minimum = min(list1)

for i in range(minimum, maximum+1):
  fuel = 0
  for j in list1:
    fuel += abs(j - i)
  if fuel < least:
      least = fuel
  print(i,fuel)

print(least)
