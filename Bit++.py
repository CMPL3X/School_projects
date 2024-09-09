Lngt = input()

x = int(0)

count = int(0)

while str(count) < str(Lngt) :
    User_Input = str(input())
    count = count + 1
    if User_Input [1] == "+" :
        x = x + 1
    if User_Input == "-" :
        x = x - 1

print(int(x))
