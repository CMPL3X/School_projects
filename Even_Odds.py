input_str = input("")
num1_str, num2_str = input_str.split()
num1 = int(num1_str)
num2 = int(num2_str)
count1 = 1
NumList = []

for _ in range(num1 // 2):
    NumList.append(count1)
    count1 = count1 + 2

num3 = num1 / num2

print(NumList[num3 - 1])