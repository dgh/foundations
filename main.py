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

def dfa_compliment(d, name):
	return DFA(name, d.Σ, d.Q, d.q0, d.δ, d.Q - d.F)

binary = Alphabet([Char('0'), Char('1')])
# alpha = Alphabet([Char(c) for c in 'abcdefghijklmnopqrstuvwxyz#"'])

even_length_dfa = DFA('even_length_dfa', binary,
					  {'q0', 'q1'}, 'q0',
					  {
					  	# 'q0': {Char('0'): 'q1', Char('1'): 'q1'},
					  	# 'q1': {Char('0'): 'q0', Char('1'): 'q0'}
					  	'q0': {'_default': 'q1'},
					  	'q1': {'_default': 'q0'}
					  },
					  {'q0'})

tests = [([], False), ([Char()], True), ('0', False), ('1', False), ('00', True), ('01', True), ('10', True), ('11', True), ('000', False), ('001', False), ('010', False), ('011', False), ('0000', True)]
run_dfa_tests(even_length_dfa, tests)
print(f'Trace of {even_length_dfa.name} with input \'0110\': {even_length_dfa.trace("0110")}')

contains_001_dfa = DFA('contains_001_dfa', binary,
					   {'q0', 'q1', 'q2', 'q3'}, 'q0',
					   {
						   	'q0': {Char('0'): 'q1', '_default': 'q0'},
						    'q1': {Char('0'): 'q2', '_default': 'q0'},
						    'q2': {Char('1'): 'q3', '_default': 'q2'},
						    'q3': {'_default': 'q3'}
					   },
					   {'q3'})

contains_001_dfa_c = dfa_compliment(contains_001_dfa, 'contains_001_dfa_c')
print(f'Accepting states of {contains_001_dfa.name}: {contains_001_dfa.F}')
contains_001_dfa = dfa_compliment(contains_001_dfa_c, 'contains_001_dfa')
print(f'Accepting states of {contains_001_dfa_c.name}: {contains_001_dfa_c.F}')