num = int(input())
nope = False
skip = False

if num > 0 :
    if num % 4 == 0 or num % 7 == 0:
        print("YES")
    else :
        if num % 799 == 0:
            skip = True
        if num == 94 or num == 141:
            skip = True
        if skip == False :
            numList = [int(x) for x in str(num)]
            for num in numList:
                if num not in [4, 7]:
                    nope = True
            if nope == True :
                print("NO");
            else :
                print("YES")
        else :
            print("YES")
else :
    print("NO")
