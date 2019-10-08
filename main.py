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
	
def test_dfa(d, s, expected):
	if d.accepts(s) != expected:
		print(f'Test of {d.name} FAILED with {s}, expected {expected} but got {not expected}!')
		return False
	return True

def run_dfa_tests(d, tests):
	passed = 0
	for test in tests:
		if test_dfa(d, String(test[0], d.Σ), test[1]):
			passed += 1
	print(f'{passed}/{len(tests)} tests PASSED for {d.name}!')
	return passed

binary = Alphabet([Char('0'), Char('1')])
alpha = Alphabet([Char(c) for c in 'abcdefghijklmnopqrstuvwxyz#"'])

even_length_dfa = DFA('even_length_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if qi == 0 and c else 0),
					  (lambda qi: qi == 0))

print('Trace of even_length_dfa with string \'0000\':')
print(even_length_dfa.trace('0000'))