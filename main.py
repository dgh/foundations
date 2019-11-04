from char import Char
from alphabet import Alphabet
from string import String
from nfa import NFA
from dfa import DFA

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

new = fa.nfa_n3.concat(fa.nfa_n4)

#print(new.accepts(String('0baa')))		# -> False
#print(new.accepts(String('00baa')))	# -> True
#print(new.accepts(String('000baa')))	# -> True

test_n = NFA('(a|b)*abb', Alphabet([Char('a'), Char('b')]),
			{'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'}, 'q0',
			{
				'q0': {'ε': ['q1', 'q7']},
				'q1': {'ε': ['q2', 'q4']},
				'q2': {Char('a'): ['q3']},
				'q3': {'ε': ['q6']},
				'q4': {Char('b'): ['q5']},
				'q5': {'ε': ['q6']},
				'q6': {'ε': ['q1', 'q7']},
				'q7': {Char('a'): ['q8']},
				'q8': {Char('b'): ['q9']},
				'q9': {Char('b'): ['q10']},
				'q10': {}
			}, {'q10'})

test_d = DFA('(a|b)*abb', Alphabet([Char('a'), Char('b')]),
			{'qA', 'qB', 'qC', 'qD', 'qE'}, 'qA',
			{
				'qA': {Char('a'): 'qB', Char('b'): 'qC'},
				'qB': {Char('a'): 'qB', Char('b'): 'qD'},
				'qC': {Char('a'): 'qB', Char('b'): 'qC'},
				'qD': {Char('a'): 'qB', Char('b'): 'qE'},
				'qE': {Char('a'): 'qB', Char('b'): 'qC'}
			}, {'qE'})
dd = test_n.toDFA()
test_string = String('babb')

# These three should all be equivalent
print(test_n.accepts(test_string))
print(test_d.accepts(test_string))
print(dd.accepts(test_string))