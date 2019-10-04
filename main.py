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
alpha = Alphabet([Char(c) for c in 'abcdefghijklmnopqrstuvwxyz#"'])

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

even_length_dfa = DFA('even_length_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if qi == 0 and c else 0),
					  (lambda qi: qi == 0))

odd_length_dfa = DFA('odd_length_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if qi == 0 and c else 0),
					  (lambda qi: qi == 1))

even_binary_dfa = DFA('even_binary_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if c == '0' else 0),
					  (lambda qi: qi == 1))

odd_binary_dfa = DFA('odd_binary_dfa', binary,
					 (lambda qi: qi == 0 or qi == 1), 0,
					 (lambda qi, c: 0 if c == '0' else 1),
					 (lambda qi: qi == 1))

dave_dfa = DFA('dave_dfa', alpha,
			   (lambda qi: qi == 0 or qi == 1 or qi == 2 or qi == 3 or qi == 4 or qi == 5), 0,
			   (lambda qi, c: 1 if qi == 0 and c == 'd' else 2 if qi == 1 and c == 'a' else 3 if qi == 2 and c == 'v' else 4 if qi == 3 and c == 'e' else 5),
			   (lambda qi: qi == 4))

python_comment_dfa = DFA('python_comment_dfa', alpha,
 						 (lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
						 (lambda qi, c: 1 if qi == 0 and c == '#' else 1 if qi == 1 else 2),
						 (lambda qi: qi == 1))

consecutive_zeros_dfa = DFA('consecutive_zeros_dfa', binary,
							(lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
							(lambda qi, c: 1 if qi == 0 and c == '0' else 2 if qi == 1 and c == '0' else 2 if qi == 2 else 0),
							(lambda qi: qi == 2))

consecutive_ones_dfa = DFA('consecutive_ones_dfa', binary,
						   (lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
						   (lambda qi, c: 1 if qi == 0 and c == '1' else 2 if qi == 1 and c == '1' else 2 if qi == 2 else 0),
						   (lambda qi: qi == 2))

valid_string_dfa = DFA('valid_string_dfa', alpha,
					   (lambda qi: qi == 0 or qi == 1 or qi == 2 or qi == 3 or qi == 4), 0,
					   (lambda qi, c: 1 if qi == 0 and c == '"' else 2 if qi == 1 and c != '"' else 3 if qi == 2 and c == '"' else 3 if qi == 1 and c == '"' else 2 if qi == 2 else 4),
					   (lambda qi: qi == 3))

contains_001_dfa = DFA('contains_001_dfa', binary,
					   (lambda qi: qi == 0 or qi == 1 or qi == 2 or qi == 3), 0,
					   (lambda qi, c: 0 if qi == 0 and c == '1' else 1 if qi == 0 and c == '0' else 0 if qi == 1 and c == '1' else 2 if qi == 1 and c == '0' else 2 if qi == 2 and c == '0' else 3),
					   (lambda qi: qi == 3))

only_ones_dfa = DFA('only_ones_dfa', binary,
					(lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
					(lambda qi, c: 1 if qi != 2 and c == '1' else 2),
					(lambda qi: qi == 1))

only_zeros_dfa = DFA('only_zeros_dfa', binary,
					 (lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
					 (lambda qi, c: 1 if qi != 2 and c == '0' else 2),
					 (lambda qi: qi == 1))