# Problem67.py

from Problem18 import shorter

file = open('triangle.txt', 'rt')

source_triangle = []
source_height = 0

for line in file:
	num_line = [ int(s) for s in line.split() ]
	source_triangle += num_line
	source_height += 1

file.close()

triangle = source_triangle

for i in range(source_height - 1):
	height = source_height - i
	triangle = shorter(triangle, height)

print(triangle[0])

# The result is 7273