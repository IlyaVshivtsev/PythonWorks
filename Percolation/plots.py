# plots.py

import matplotlib.pyplot as plt

file_names	= ['percolation2d.txt', 'percolation3d.txt']
titles		= ['Conduction Probability: 2d', 'Conduction Probability: 3d']

for file_name, title in zip(file_names, titles):

	file = open(file_name, 'rt')

	args  = []
	vals1 = []
	vals2 = []
	vals3 = []

	for line in file:
		line = line.split(' ')
		arg  = float(line[0])
		val1 = float(line[1])
		val2 = float(line[2])
		val3 = float(line[3])

		args.append(arg)
		vals1.append(val1)
		vals2.append(val2)
		vals3.append(val3)

	file.close()

	plt.title(title)
	plt.plot(args, vals1, args, vals2, args, vals3)
	plt.show()