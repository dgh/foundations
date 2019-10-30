from char import Char
from alphabet import Alphabet
from string import String
from nfa import NFA

import tests as fa

def run_dfa_tests(d, tests):
	def test_dfa(d, s, expected):
		if d.accepts(s) != expected:
			print(f'Test of {d.name} FAILED with {s}, expected {expected} but got {not expected}!')
			return False
		return True
	
	passed = 0
	for case in tests:
		if test_dfa(d, String(case[0]), case[1]):
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

def run_dfa_equality_tests(d1, tests):
	def test_dfa_equality(d1, d2, expected):
		if (d1 == d2) != expected :
			print(f'Test if {d1.name} == {d2.name} FAILED, expected {expected} but got {not expected}!')
			return False
		return True

	passed = 0
	for case in tests:
		if test_dfa_equality(d1, case[0], case[1]):
			passed += 1
	print(f'{passed}/{len(tests)} equality tests PASSED for {d1.name}!')
	return passed

binary = fa.binary
alpha = fa.alpha

abc_alpha = Alphabet([Char('a'), Char('b'), Char('c')])

test_nfa = NFA('test_nfa', binary,
				 {'qA', 'qB', 'qC', 'qD'}, 'qA',
				 {
				 	'qA': {Char('0'): ['qA', 'qB'], Char('1'): ['qC']},
				 	'qB': {Char('0'): ['qB'], Char('1'): ['qB'], 'ε': ['qD']},
				 	'qC': {Char('0'): ['qD'], Char('1'): ['qC']},
				 	'qD': {Char('0'): ['qD'], Char('1'): ['qD']}
				 },
				 {'qD'})

test_string = String('0110')

new_nfa = NFA.fromDFA('nfa_even_length', fa.even_length)
new_nfa_2 = NFA('nfa_even_length_2', binary,
						 {'q0', 'q1'}, 'q0',
						 {
						 	'q0': {Char('0'): ['q1'], Char('1'): ['q1']},
						 	'q1': {Char('0'): ['q0'], Char('1'): ['q0']}
						 },
						 {'q0'})