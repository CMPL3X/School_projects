input_str = input("")
num1_str, num2_str = input_str.split()
num1 = int(num1_str)
num2 = int(num2_str) - 1
var1 = 0
count1 = 1
NumListOdd = []
NumListEven = []

for _ in range(num1 // 2):
    NumListOdd.append(count1)
    count1 = count1 + 2

for _ in range(num1 // 2 - 1):
    NumListEven.append(count1)
    count1 = count1 + 2


# 1) all odd 1 to N
# 2) all even 1 to N
# 3) kurš ir K, ja 1<=K<=N<=100000


if num2 < len(NumListOdd):
    print(NumListOdd[num2])
else:
    print(NumListOdd)
    var1 = int(num2 / len(NumListOdd))
    print("var 1 is " + str(var1))
    print(NumListOdd[var1])
