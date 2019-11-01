from char import Char
from alphabet import Alphabet
from string import String
from nfa import NFA

import fa

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

t = fa.nfa_n1.union(fa.nfa_n2)

print(t.accepts(String('1001'))) # -> False
print(t.accepts(String('111'))) # -> True