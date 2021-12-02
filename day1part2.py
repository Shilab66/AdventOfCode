file = open("Day1Part1.txt", "r")
last = None
increased = 0;
array1 = []

for x in file:
    if last == None:
        last = int(x);
        continue;
    elif int(x) > last:
        increased += 1
        last = int(x);
        print(int(x))
    else:
        last = int(x);

#print(array1)
print("Increased: " + str(increased))
