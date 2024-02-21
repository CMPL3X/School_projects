num = int(input())
x = 0
count = True
FinalLine = ""

if num == 1:
    FinalLine = "I hate"
    x = 1

while x <= num:
    if x == 0:
        FinalLine = "I hate"
        x = x + 1
    if x < 0:
        if count == False :
            FinalLine = FinalLine + " that I hate"
            count == True
            x = x + 1
        if count == True :
            FinalLine = FinalLine + " that I love"
            count == False
            x = x + 1

print(str(FinalLine) + " it")
