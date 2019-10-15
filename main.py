from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA
from nfa import NFA

from pprint import pprint
import tests as fa

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

binary = fa.binary
alpha = fa.alpha

test_nfa = NFA('test_nfa', binary,
				 {'qA', 'qB', 'qC', 'qD'}, 'qA',
				 {
				 	'qA': {Char('0'): ['qB'], Char('1'): ['qC']},
				 	'qB': {Char('0'): ['qB'], Char('1'): ['qB'], 'ε': ['qD']},
				 	'qC': {Char('0'): ['qD'], Char('1'): ['qC']},
				 	'qD': {Char('0'): ['qD'], Char('1'): ['qD']}
				 },
				 {'qD'})

print(test_nfa.accepts(String([Char('1'), Char('1'), Char('0'), Char('1')], binary)))

test_cases = [([], False), ('0', True), ('1', False), ('00', True), ('01', False), ('10', True), ('11', False), ('000', True), ('001', False), ('010', True), ('011', False), ('1110', True)]
#run_dfa_tests(even_binary, test_cases)