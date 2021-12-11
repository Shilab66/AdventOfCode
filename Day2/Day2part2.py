file = open("Day2Part1Fipe2.txt", "r")
depth = 0
horizontal = 0
aim = 0
line = 0

for i in file:
  line += 1
  list1 = i.split(" ")

  #print("\nType: " + str(list1[0].strip()) + "\nValue: " + str(list1[1].strip()) + "\nLine: " + str(line))

  if list1[0].strip(" ") == "down":
    print("Down : " + str((list1[1].strip())))
    aim += int(list1[1].strip())
  elif list1[0].strip(" ") == "up":
    print("Up : " + str((list1[1].strip())))
    aim -= int(list1[1].strip())
  elif list1[0].strip(" ") == "forward":
    print("Forward : " + str((list1[1].strip())))
    horizontal += int(list1[1].strip())
    depth += aim * int(list1[1].strip())

print(depth * horizontal)
