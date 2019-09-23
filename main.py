import math
from itertools import product

from char import Char
from alphabet import Alphabet
from string import String


alphabet = Alphabet([Char('0'), Char('1')])
test_string = String([Char('0'), Char('1')], alphabet)

def generate_nth_string(a, n):
	if not n: return String([Char()], a)
	# |A|^l
	l = int(math.log(n + 1, len(a))) # l = layer
	i =  n + 1 - len(a) ** l # i = layer index + 1
	return String(list(product(a, repeat=l))[i], a)

for i in range(0, 31):
	print('{}:\t{}'.format(i, generate_nth_string(alphabet, i)))