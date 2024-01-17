num = int(input())

if num > 0 :
    if num % 4 == 0 or num % 7 == 0:
        print("YES")
    else :
        numList = [int(x) for x in str(num)]
        if numList != 4 and numList != 7:
            print("NO2")
        else :
            print("YES2")
else :
    print("NO")
