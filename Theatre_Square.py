import math

input_line = input()

input_line_split = input_line.split(" ")

n = int(input_line_split[0])

m = int(input_line_split[1])

a = int(input_line_split[2])

print( math.ceil( m / a ) * math.ceil( n / a ) )