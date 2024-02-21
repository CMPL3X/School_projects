num = int(input())
x = int(0)
count = True
FinalLine = ""

if num == 1:
    FinalLine = "I hate"
    x = 1

if num != 1:
    while x < num:
        if x == 0:
            FinalLine = "I hate"
            x = x + 1
        if x > 0:
            skip = False
            if skip == False:
                if count == True :
                    FinalLine = FinalLine + " that I love"
                    count = False
                    x = x + 1
                    skip = True
            if skip == False:
                if count == False :
                    FinalLine = FinalLine + " that I hate"
                    count = True
                    x = x + 1
                    skip = True

print(str(FinalLine) + " it")
