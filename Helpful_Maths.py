input = input()

split = input.split("+")
sorted = sorted(split)

count = 1
ino = True

final = str(sorted[0])

while ino == True :
    if len(input) >= 2 :
        final = str(final) + "+" + str(sorted[count])
        count = count + 1
    if int(count) >= int(len(split)) :
        ino = False

print(final)