matrix = []
while True:
  line = input()
  if not line:
    break
  row = list(map(int, line.split()))
  matrix.append(row)

for i, row in enumerate(matrix):
  if 1 in row:
    x = row.index(1)
    y = i
    break

x = x + 1

# x pasaka x poz un y pasaka y poz
# jadabu lai x ir 3 un y ir 3
# kamer strada loop katru soli pieskaita