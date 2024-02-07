num = int(input(""))
limit = True
count = 0
FinList = []

while limit:
    Word = str(input(""))
    CharList = [char for char in Word]
    if len(CharList) <= 10:
        FinList.append(Word)
    if len(CharList) > 10:
        FTwoChar= ''.join(CharList[:1])
        LTwoChar= ''.join(CharList[-1:])
        FinList.append(FTwoChar + str(len(CharList) - 2) + LTwoChar)
    count = count + 1
    if count == num :
        limit = False
        for Words in FinList:
            print(Words)