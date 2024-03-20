input_num = int(input())
i = 0

while i < input_num:
  num1_str, num2_str, num3_str = input().split()
  num1 = int(num1_str)
  num2 = int(num2_str)
  num3 = int(num3_str)
  if num1 + num2 == num3 or num1 + num3 == num2 or num2 + num3 == num1:
    print("yes")
  else:
    print("no")
  i = i + 1
