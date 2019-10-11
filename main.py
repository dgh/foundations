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

#test_cases = [([], False), ('dave', True), ('jay', False), ('evad', False), ('daved', False), ('d', False), ('a', False), ('v', False), ('e', False), ('#dave', False), ('', False), ('#', False)]
#run_dfa_tests(dfas.dave, test_cases)

# print('has_a_zero ⊆ even_binary =>', dfas.has_a_zero in dfas.even_binary) # Expected to be False 
# print('even_binary ⊆ has_a_zero =>', dfas.even_binary in dfas.has_a_zero) # Expected to be True 

print('even_length ⊆ odd_length =>', dfas.even_length in dfas.odd_length) # Expected to be False but return True
print('odd_length ⊆ even_length =>', dfas.odd_length in dfas.even_length) # Expected to be False returns False
print('even_length == odd_length =>', dfas.even_length == dfas.odd_length) # Expected to be False returns False

print('even_length ⊆ consecutive_ones_and_contains_001 =>', dfas.even_length in dfas.consecutive_ones_and_contains_001) # Expected to be False because '00' which is in even_length is not a part of consecutive_ones_and_contains_001

# Outputing examples of what are acceptable strings from each. The first eight of even_length are not found in consecutive_ones_and_contains_001
print('\n'*2)
print('even_length = {')
for x in range(48):
	s = binary.generate_nth_string(x)
	if dfas.even_length.accepts(s):
		print('\t', s)
print('}')
print('consecutive_ones_and_contains_001 = {')
for x in range(48):
	s = binary.generate_nth_string(x)
	if dfas.consecutive_ones_and_contains_001.accepts(s):
		print('\t', s)
print('}')