Lngt = int(input())

x = 0

count = 0

while count < Lngt :
    User_Input = str(input())
    count = count + 1
    if User_Input [1] == "+" :
        x = x + 1
    if User_Input [1] == "-" :
        x = x - 1

print(int(x))
