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

nfa_manual = NFA('ntest', binary,
				{'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'}, 'A',
				{
					'A': {'ε': ['B', 'H']},
					'B': {'ε': ['C', 'D']},
					'C': {Char('1'): ['E']},
					'D': {Char('0'): ['F']},
					'E': {'ε': ['G']},
					'F': {'ε': ['G']},
					'G': {'ε': ['A', 'H']},
					'H': {'ε': ['I']},
					'I': {Char('1'): ['J']},
					'J': {}
				}, {'J'})

dfa_manual = DFA('fsa', binary,
				{'A', 'B', 'C'}, 'A',
				{
					'A': {Char('0'): 'B', Char('1'): 'C'},
					'B': {Char('0'): 'B', Char('1'): 'C'},
					'C': {Char('0'): 'B', Char('1'): 'C'},
				}, {'C'})

dfa_from_nfa = nfa_manual.toDFA('dfa_from_nfa')

# for x in range(1, 16):
# 	s = binary.generate_nth_string(x)
# 	print(s, '=>', nfa_manual.accepts(s), dfa_from_nfa.accepts(s))

# print("The toDFA function works:", dfa_from_nfa == dfa_manual)

nfa_fork = NFA('nfa_fork', binary,
				{'A', 'B', 'C', 'D', 'E'}, 'A',
				{
					'A': {Char('0'): ['A'], Char('1'): ['A', 'B']},
					'B': {Char('0'): ['C'], Char('1'): ['C']},
					'C': {Char('0'): ['D'], Char('1'): ['D']},
					'D': {Char('0'): ['E'], Char('1'): ['E']},
					'E': {Char('0'): ['E'], Char('1'): ['E']}
				}, {'D'})

trace_tree1 = '(A [(0/A [(1/A [(0/A [(0/A [NO])])])(1/B [(0/C [(0/D [YES])])])])])'
trace_tree2 = '(A[(1/A[(0/A[(1/A[(0/A[(0/A[NO])])])(1/B[(0/C[(0/D[YES])])])])])(1/B[(0/C[(1/D[(0/E[(0/E[NO])])])])])])'
trace_tree3 = '(A[(0/A[(0/A[(0/A[(0/A[NO])])])])])'
trace_tree4 = '(A[(0/A[(0/A[(0/A[(0/A[NO])])])])])'
trace_tree5 = '(A[(1/A[(0/A[NO])])(1/B[(0/C[NO])])])'
trace_tree6 = '(A[(1/A[(0/A[(0/A[(1/A[(0/A[(0/A[NO])])])(1/B[(0/C[(0/D[YES])])])])])])(1/B[(0/C[(0/D[(1/E[(0/E[(0/E[NO])])])])])])])'
