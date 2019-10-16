from string import String
from itertools import product

class Alphabet(list):
	def __init__(self, data=[]):
		super(Alphabet, self).__init__(data)

	def is_empty(self):
		return not len(self)

	def generate_nth_string(self, n):
		if n == 1: return String([])

		total_size = 1
		layer_size = 1
		layer = 0

		while True:
			layer_size = total_size
			total_size += len(self) ** (layer + 1)
			if n <= total_size:
				break
			layer += 1

		index = n - layer_size - 1

		return String(list(product(self, repeat=layer + 1))[index])

	def __repr__(self):
		return 'Alphabet<{}>'.format(', '.join(map(str, self)))