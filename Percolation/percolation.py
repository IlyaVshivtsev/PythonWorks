# percolation.py

import numpy as np

def create(shape, p):
	'''
	Creates a new matrix
	'''
	return np.random.choice([True, False], shape, p=[p, 1.0-p])

def print_matrix(matrix):
	'''
	Prints 2d-matrix
	'''
	for row in matrix:
		for element in row:
			print(int(element), end=' ')
		print()

def is_permeable(matrix):
	'''
	Finds out if the matrix is permeable
	'''
	res = False

	for point in np.ndindex(matrix[0].shape):
		point = (0,) + point
		res = is_point_good(matrix, point)
		if res:
			break

	return res 

def is_point_good(matrix, point):
	'''
	Finds out if the point in the matrix is good
	'''
	if not matrix[point]:
		return False

	if point[0] == matrix.shape[0]-1:
		return True

	matrix[point] = False

	res = False

	for i in range(matrix.ndim):

		if point[i]+1 < matrix.shape[i]:
			new_point = point[:i] + (point[i]+1,) + point[i+1:]

			res = is_point_good(matrix, new_point)
			if res:
				break

		if point[i] > 0:
			new_point = point[:i] + (point[i]-1,) + point[i+1:]

			res = is_point_good(matrix, new_point)
			if res:
				break

	return res

def p_cond(p, k, shape):
	'''
	Computes the probability of matrix conductivity
	'''
	res = 0.0

	for i in range(k):
		matrix = create(shape, p)

		if is_permeable(matrix):
			res += 1.0

	res /= k

	return res

def main():

	k = 10000

	file2d = open('percolation2d.txt', 'wt')
	file3d = open('percolation3d.txt', 'wt')

	ps = np.linspace(start=0.0, stop=1.0, num=129)

	for p in ps:

		v1 = p_cond(p, k, shape=(10,10))
		v2 = p_cond(p, k, shape=(15,15))
		v3 = p_cond(p, k, shape=(20,20))
		print('%f %f %f %f\n' % (p,v1,v2,v3))
		file2d.write('%f %f %f %f\n' % (p,v1,v2,v3))

		v1 = p_cond(p, k, shape=(5,5,5))
		v2 = p_cond(p, k, shape=(7,7,7))
		v3 = p_cond(p, k, shape=(10,10,10))
		print('%f %f %f %f\n' % (p,v1,v2,v3))
		file3d.write('%f %f %f %f\n' % (p,v1,v2,v3))

	file2d.close()
	file3d.close()

if __name__ == '__main__':
	main()