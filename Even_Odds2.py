n, k = map(int, input().split())

if k <= (n + 1) // 2:
   result = k * 2 - 1
else:
   result = (k - (n + 1) // 2) * 2

print(result)