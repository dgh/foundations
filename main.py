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
				 	'qA': {Char('0'): ['qB'], Char('1'): ['qC']},
				 	'qB': {Char('0'): ['qB'], Char('1'): ['qB'], 'ε': ['qD']},
				 	'qC': {Char('0'): ['qD'], Char('1'): ['qC']},
				 	'qD': {Char('0'): ['qD'], Char('1'): ['qD']}
				 },
				 {'qD'})

test_string = String([Char('0'), Char('0')])
print(test_nfa.name, 'should accept: ', test_string, '=>', test_nfa.accepts(test_string))

#print(fa.odd_binary.get_accepted())
#print(fa.odd_binary.accepts(fa.odd_binary.get_accepted()))


print('Results:')
A = []
B = []
for i in range(1, 200):
	s = binary.generate_nth_string(i)
	if fa.union_test.accepts(s):
		A.append(s)
	if fa.odd_number_of_ones.intersect(fa.even_length).accepts(s):
		B.append(s)

print(A)
print(B)

for s in A:
	if not (s in B):
		print(s)