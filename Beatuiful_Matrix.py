matrix = []
counter = 0
while True:
  line = input()
  row = list(map(int, line.split()))
  matrix.append(row)
  if counter == 4:
    break
  counter = counter + 1

for i, row in enumerate(matrix):
  if 1 in row:
    x = row.index(1)
    y = i
    break

x = x + 1
y = y + 1
num = 0
lock = True

while (lock == True) :
  if x > 3 :
    x = x - 1
    num = num + 1

  if x < 3 :
    x = x + 1
    num = num + 1

  while x == 3 :
    if y > 3 :
      y = y - 1
      num = num + 1

    if y < 3 :
      y = y + 1
      num = num + 1

    if y == 3 :
      print( num )
      lock = False
      break