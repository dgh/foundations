from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA

import tests as dfas

def cross(d1, d2, cond, name):
	states = set()
	accepts = set()
	delta = dict()

	for qi1 in d1.Q:
		for qi2 in d2.Q:
			states.add((qi1, qi2))
			delta[(qi1, qi2)] = dict()
			for c in d1.Σ:
				delta[(qi1, qi2)][c] = (d1.δ[qi1][c], d2.δ[qi2][c])

	for (qi1, qi2) in states:
		if cond(qi1 in d1.F, qi2 in d2.F):
			accepts.add((qi1, qi2))

	return DFA(name, d1.Σ, states, (d1.q0, d2.q0), delta, accepts)

def union(d1, d2):
	return cross(d1, d2, bool.__or__, f'{d1.name}_or_{d2.name}')

def intersect(d1, d2):
	return cross(d1, d2, bool.__and__, f'{d1.name}_and_{d2.name}')

def complement(d1):
	return DFA(f'{d1.name}_c', d1.Σ, d1.Q, d1.q0, d1.δ, d1.Q - d1.F)

def subset(A, B):
	if intersect(A, complement(B)).get_accepted():
		return False
	return True

def equal(d1, d2):
	return subset(d1, d2) and subset(d2, d1)

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
		if subset(d1, d2) != expected:
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

#test_cases = [([], False), ('dave', True), ('jay', False), ('evad', False), ('daved', False), ('d', False), ('a', False), ('v', False), ('e', False), ('#dave', False), ('', False), ('#', False)]
#run_dfa_tests(dfas.dave, test_cases)

# print('has_a_zero ⊆ even_binary =>', dfas.has_a_zero in dfas.even_binary) # Expected to be False 
# print('even_binary ⊆ has_a_zero =>', dfas.even_binary in dfas.has_a_zero) # Expected to be True 

print('even_length ⊆ odd_length =>', subset(dfas.even_length, dfas.odd_length)) # Expected to be False but return True
print('odd_length ⊆ even_length =>', subset(dfas.odd_length, dfas.even_length)) # Works, False
print('even_length == odd_length =>', equal(dfas.even_length, dfas.odd_length)) # Works, False

print('even_length ⊆ consecutive_ones_and_contains_001 =>', subset(dfas.even_length, dfas.consecutive_ones_and_contains_001)) # Expected to be False because '00' which is in even_length is not a part of consecutive_ones_and_contains_001

# Outputing examples of what are acceptable strings from each. The first eight of even_length are not found in consecutive_ones_and_contains_001
# print('\n'*2)
# print('even_length = {')
# for x in range(48):
# 	s = binary.generate_nth_string(x)
# 	if dfas.even_length.accepts(s):
# 		print('\t', s)
# print('}')
# print('consecutive_ones_and_contains_001 = {')
# for x in range(48):
# 	s = binary.generate_nth_string(x)
# 	if dfas.consecutive_ones_and_contains_001.accepts(s):
# 		print('\t', s)
# print('}')