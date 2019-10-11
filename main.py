from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA

import tests as dfas

def test_dfa(d, s, expected):
	if d.accepts(s) != expected:
		print(f'Test of {d.name} FAILED with {s}, expected {expected} but got {not expected}!')
		return False
	return True

def run_dfa_tests(d, cases):
	passed = 0
	for test in cases:
		if test_dfa(d, String(test[0], d.Σ), test[1]):
			passed += 1
	print(f'{passed}/{len(cases)} tests PASSED for {d.name}!')
	return passed

binary = dfas.binary
alpha = dfas.alpha

test_cases = [([], False), ('dave', True), ('jay', False), ('evad', False), ('daved', False), ('d', False), ('a', False), ('v', False), ('e', False), ('#dave', False), ('', False), ('#', False)]
run_dfa_tests(dfas.dave, test_cases)

print('has_a_zero ⊆ even_binary =>', dfas.even_binary.subset(dfas.has_a_zero))
print('even_binary ⊆ has_a_zero =>', dfas.even_binary in (dfas.has_a_zero))