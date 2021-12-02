file = open("Day1Part1.txt", "r")
last = None
last2 = None
first = 0
increased = 0;
array1 = []

for x in file:
    if first < 2:
        first += 1
        last2=last
        last=int(x)
        continue
    else:
        array1.append(last2+last+int(x))
        last2=last
        last=int(x)

last = None

for x in array1:
    if last == None:
        last = int(x);
        continue;
    elif int(x) > last:
        increased += 1
        last = int(x);
        print(int(x))
    else:
        last = int(x);

print("Increased: " + str(increased))