num = int(input())
nope = False

if num > 0 :
    if num % 4 == 0 or num % 7 == 0:
        print("YES")
    else :
        numList = [int(x) for x in str(num)]
        for num in numList:
            if num not in [4, 7]:
                nope = True
        if nope == True :
            print("NO");
        else :
            print("YES")
else :
    print("NO")
