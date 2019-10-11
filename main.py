from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA

import tests as dfas

def run_dfa_tests(d, tests):
	def test_dfa(d, s, expected):
		if d.accepts(s) != expected:
			print(f'Test of {d.name} FAILED with {s}, expected {expected} but got {not expected}!')
			return False
		return True
	
	passed = 0
	for case in tests:
		if test_dfa(d, String(case[0], d.Σ), case[1]):
			passed += 1
	print(f'{passed}/{len(tests)} tests PASSED for {d.name}!')
	return passed

def run_dfa_subset_tests(d1, tests):
	def test_dfa_subset(d1, d2, expected):
		if (d1 in d2) != expected:
			print(f'Test if {d1.name} ⊆ {d2.name} FAILED, expected {expected} but got {not expected}!')
			return False
		return True

	passed = 0
	for case in tests:
		if test_dfa_subset(d1, case[0], case[1]):
			passed += 1
	print(f'{passed}/{len(tests)} subset tests PASSED for {d1.name}!')
	return passed

binary = dfas.binary
alpha = dfas.alpha

test_cases = [([], False), ('dave', True), ('jay', False), ('evad', False), ('daved', False), ('d', False), ('a', False), ('v', False), ('e', False), ('#dave', False), ('', False), ('#', False)]
#run_dfa_tests(dfas.dave, test_cases)

print('has_a_zero ⊆ even_binary =>', dfas.has_a_zero in dfas.even_binary)
print('has_a_zero ⊆ even_binary =>', dfas.even_binary in dfas.has_a_zero)
print('even_binary ⊆ has_a_zero =>', dfas.even_binary in dfas.has_a_zero)
print('even_binary ⊆ has_a_zero =>', dfas.has_a_zero in dfas.even_binary)