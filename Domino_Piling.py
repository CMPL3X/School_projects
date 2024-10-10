import math

input_line = input()

input_line_split = input_line.split(" ")

N = int(input_line_split[0])

M = int(input_line_split[1])

print(math.floor((N*M)/2))