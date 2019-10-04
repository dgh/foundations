import math
from itertools import product
from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA

def generate_nth_string(a, n):
	if not n: return String([Char()], a)
	# |A|^l
	l = int(math.log(n + 1, len(a))) # l = layer
	i =  n + 1 - len(a) ** l # i = layer index + 1
	return String(list(product(a, repeat=l))[i], a)

binary = Alphabet([Char('0'), Char('1')])

no_strings_dfa = DFA('no_strings_dfa', binary,
					 (lambda qi: False), 0,
					 (lambda qi, c: False),
					 (lambda qi: False))

empty_string_dfa = DFA('empty_string_dfa', binary,
					   (lambda qi: qi == 0 or qi == 1), 0,
					   (lambda qi, c: 1 if c else 0),
					   (lambda qi: qi == 0))

only_one_char_dfa = DFA('only_one_char_dfa', binary,
						(lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
						(lambda qi, c: 1 if qi == 0 and c else 2),
						(lambda qi: qi == 1))