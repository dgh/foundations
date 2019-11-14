from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA
from nfa import NFA

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
		if (d1 == d2) != expected:
			print(f'Test if {d1.name} == {d2.name} FAILED, expected {expected} but got {not expected}!')
			return False
		return True

	passed = 0
	for case in tests:
		if test_dfa_equality(d1, case[0], case[1]):
			passed += 1
	print(f'{passed}/{len(tests)} equality tests PASSED for {d1.name}!')
	return passed

traces_cases = [
		([(Char('0'), 'q1'), (Char('1'), 'q2'), (Char('0'), 'q3'), (Char('1'), 'q4'), (Char('1'), 'q4'), (Char('0'), 'q4')], True),
		([(Char('1'), 'q2'), (Char(), 'q3'), (Char('1'), 'q4')], True),
		([(Char('1'), 'q1'), (Char('0'), 'q1'), (Char('1'), 'q2'), (Char('0'), 'q3'), (Char('1'), 'q4')], True)
	]

def run_nfa_oracle_test(n1, tests):
	def test_nfa_oracle(n1, s, t, expected):
		if not n1.oracle(s, t, expected):
			print(f'Test {n1.name}.oracle() FAILED, expected {expected} but got {not expected}!')
			return False
		return True

	passed = 0
	for case in tests:
		s = String([t[0] for t in case[0]])
		if test_nfa_oracle(n1, s, case[0], case[1]):
			passed += 1
	print(f'{passed}/{len(tests)} oracle tests PASSED for {n1.name}!')
	return passed	

binary = Alphabet([Char('0'), Char('1')])
alpha = Alphabet([Char(c) for c in 'adejyv#"'])

no_strings = DFA('no_strings', binary,
				{'q0', 'q1'}, 'q0',
				{
					'q0': {Char('0'): 'q0', Char('1'): 'q0'},
					'q1': {Char('0'): 'q1', Char('1'): 'q1'}
				},
				{'q1'})

empty_string = DFA('empty_string', binary,
				{'q0', 'q1'}, 'q0',
				{
					'q0': {Char('0'): 'q1', Char('1'): 'q1'},
					'q1': {Char('0'): 'q1', Char('1'): 'q1'}
				},
				{'q0'})

only_one_char = DFA('only_one_char', binary,
					{'q0', 'q1', 'q2'}, 'q0',
					{
						'q0': {Char('0'): 'q1', Char('1'): 'q1'},
						'q1': {Char('0'): 'q2', Char('1'): 'q2'},
						'q2': {Char('0'): 'q2', Char('1'): 'q2'}
					},
					{'q1'})

even_length = DFA('even_length', binary,
				{'q0', 'q1'}, 'q0',
				{
					'q0': {Char('0'): 'q1', Char('1'): 'q1'},
					'q1': {Char('0'): 'q0', Char('1'): 'q0'}
				},
				{'q0'})

odd_length = DFA('odd_length', binary,
				{'q0', 'q1'}, 'q0',
				{
					'q0': {Char('0'): 'q1', Char('1'): 'q1'},
					'q1': {Char('0'): 'q0', Char('1'): 'q0'}
				},
				{'q1'})

even_binary = DFA('even_binary', binary,
				{'q0', 'q1', 'q2'}, 'q0',
				{
					'q0': {Char('0'): 'q2', Char('1'): 'q1'},
					'q1': {Char('0'): 'q2', Char('1'): 'q1'},
					'q2': {Char('0'): 'q2', Char('1'): 'q1'}
				},
				{'q2'})

odd_binary = DFA('odd_binary', binary,
				{'q0', 'q1', 'q2'}, 'q0',
				{
					'q0': {Char('0'): 'q2', Char('1'): 'q1'},
					'q1': {Char('0'): 'q2', Char('1'): 'q1'},
					'q2': {Char('0'): 'q2', Char('1'): 'q1'}
				},
				{'q1'})

consecutive_zeros = DFA('consecutive_zeros', binary,
						{'q0', 'q1', 'q2'}, 'q0',
						{
							'q0': {Char('0'): 'q1', Char('1'): 'q0'},
							'q1': {Char('0'): 'q2', Char('1'): 'q0'},
							'q2': {Char('0'): 'q2', Char('1'): 'q2'}
						},
						{'q2'})

consecutive_ones = DFA('consecutive_ones', binary,
					{'q0', 'q1', 'q2'}, 'q0',
					{
						'q0': {Char('1'): 'q1', Char('0'): 'q0'},
						'q1': {Char('1'): 'q2', Char('0'): 'q0'},
						'q2': {Char('1'): 'q2', Char('0'): 'q2'},
					},
					{'q2'})

contains_001 = DFA('contains_001', binary,
				{'q0', 'q1', 'q2', 'q3'}, 'q0',
				{
						'q0': {Char('0'): 'q1', Char('1'): 'q0'},
						'q1': {Char('0'): 'q2', Char('1'): 'q0'},
						'q2': {Char('0'): 'q2', Char('1'): 'q3'},
						'q3': {Char('0'): 'q3', Char('1'): 'q3'}
				},
				{'q3'})

only_ones = DFA('only_ones', binary,
				{'q0', 'q1', 'q2'}, 'q0',
				{
					'q0': {Char('0'): 'q2', Char('1'): 'q1'},
					'q1': {Char('0'): 'q2', Char('1'): 'q1'},
					'q2': {Char('0'): 'q2', Char('1'): 'q2'}
				},
				{'q1'})

only_zeros = DFA('only_zeros', binary,
				{'q0', 'q1', 'q2'}, 'q0',
				{
					'q0': {Char('0'): 'q1', Char('1'): 'q2'},
					'q1': {Char('0'): 'q1', Char('1'): 'q2'},
					'q2': {Char('0'): 'q2', Char('1'): 'q2'}
				},
				{'q1'})

dave = DFA('dave', alpha,
		{'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}, 'q0',
		{
			'q0': {Char('a'): 'q5', Char('d'): 'q1', Char('e'): 'q5', Char('j'): 'q5', Char('y'): 'q5', Char('v'): 'q5', Char('#'): 'q5', Char('"'): 'q5'},
			'q1': {Char('a'): 'q2', Char('d'): 'q5', Char('e'): 'q5', Char('j'): 'q5', Char('y'): 'q5', Char('v'): 'q5', Char('#'): 'q5', Char('"'): 'q5'},
			'q2': {Char('a'): 'q5', Char('d'): 'q5', Char('e'): 'q5', Char('j'): 'q5', Char('y'): 'q5', Char('v'): 'q3', Char('#'): 'q5', Char('"'): 'q5'},
			'q3': {Char('a'): 'q5', Char('d'): 'q5', Char('e'): 'q4', Char('j'): 'q5', Char('y'): 'q5', Char('v'): 'q5', Char('#'): 'q5', Char('"'): 'q5'},
			'q4': {Char('a'): 'q5', Char('d'): 'q5', Char('e'): 'q5', Char('j'): 'q5', Char('y'): 'q5', Char('v'): 'q5', Char('#'): 'q5', Char('"'): 'q5'},
			'q5': {Char('a'): 'q5', Char('d'): 'q5', Char('e'): 'q5', Char('j'): 'q5', Char('y'): 'q5', Char('v'): 'q5', Char('#'): 'q5', Char('"'): 'q5'}
		},
		{'q4'})

comment = DFA('comment', alpha,
			{'q0', 'q1', 'q2'}, 'q0',
			{
				'q0': {Char('a'): 'q2', Char('d'): 'q2', Char('e'): 'q2', Char('j'): 'q2', Char('y'): 'q2', Char('v'): 'q2', Char('#'): 'q1', Char('"'): 'q2'},
				'q1': {Char('a'): 'q1', Char('d'): 'q1', Char('e'): 'q1', Char('j'): 'q1', Char('y'): 'q1', Char('v'): 'q1', Char('#'): 'q1', Char('"'): 'q1'},
				'q2': {Char('a'): 'q2', Char('d'): 'q2', Char('e'): 'q2', Char('j'): 'q2', Char('y'): 'q2', Char('v'): 'q2', Char('#'): 'q2', Char('"'): 'q2'}
			},
			{'q1'})

valid_string = DFA('valid_string', alpha,
				{'q0', 'q1', 'q2', 'q3', 'q4'}, 'q0',
				{
					'q0': {Char('a'): 'q4', Char('d'): 'q4', Char('e'): 'q4', Char('j'): 'q4', Char('y'): 'q4', Char('v'): 'q4', Char('#'): 'q4', Char('"'): 'q1'},
					'q1': {Char('a'): 'q2', Char('d'): 'q2', Char('e'): 'q2', Char('j'): 'q2', Char('y'): 'q2', Char('v'): 'q2', Char('#'): 'q2', Char('"'): 'q3'},
					'q2': {Char('a'): 'q2', Char('d'): 'q2', Char('e'): 'q2', Char('j'): 'q2', Char('y'): 'q2', Char('v'): 'q2', Char('#'): 'q2', Char('"'): 'q3'},
					'q3': {Char('a'): 'q4', Char('d'): 'q4', Char('e'): 'q4', Char('j'): 'q4', Char('y'): 'q4', Char('v'): 'q4', Char('#'): 'q4', Char('"'): 'q4'},
					'q4': {Char('a'): 'q4', Char('d'): 'q4', Char('e'): 'q4', Char('j'): 'q4', Char('y'): 'q4', Char('v'): 'q4', Char('#'): 'q4', Char('"'): 'q4'}
				},
				{'q3'})

has_a_zero = DFA('has_a_zero', binary,
				{'q0', 'q1', 'q2'}, 'q0',
				{
					'q0': {Char('0'): 'q1', Char('1'): 'q2'},
					'q1': {Char('0'): 'q1', Char('1'): 'q1'},
					'q2': {Char('0'): 'q1', Char('1'): 'q2'}
				},
				{'q1'})

odd_number_of_ones = DFA('odd_number_of_ones', binary,
						{'q0', 'q1'}, 'q0',
						{
							'q0': {Char('0'): 'q0', Char('1'): 'q1'},
							'q1': {Char('0'): 'q1', Char('1'): 'q0'}
						},
						{'q1'})

nfa_fork = NFA('nfa_fork', binary,
				{'A', 'B', 'C', 'D'}, 'A',
				{
					'A': {Char('0'): ['A'], Char('1'): ['A', 'B']},
					'B': {Char('0'): ['C'], Char('1'): ['C']},
					'C': {Char('0'): ['D'], Char('1'): ['D']},
					'D': {},
				}, {'D'})

consecutive_ones_or_contains_001 = consecutive_ones.union(contains_001)
even_length_or_only_ones = even_length.union(only_ones)

consecutive_ones_and_contains_001 = consecutive_ones.intersect(contains_001)
even_length_and_only_ones = even_length.intersect(only_ones)

intersect_test = odd_number_of_ones.intersect(even_length)
intersect_test_manual = DFA('intersect_test_manual', binary,
							{('q0', 'q0'), ('q0', 'q1'), ('q1', 'q0'), ('q1', 'q1')}, ('q0', 'q0'),
							{
								('q0', 'q0'): {Char('0'): ('q0', 'q1'), Char('1'): ('q1', 'q1')},
								('q0', 'q1'): {Char('0'): ('q0', 'q0'), Char('1'): ('q1', 'q0')},
								('q1', 'q0'): {Char('0'): ('q1', 'q1'), Char('1'): ('q0', 'q1')},
								('q1', 'q1'): {Char('0'): ('q1', 'q0'), Char('1'): ('q0', 'q0')}
							},
							{('q1', 'q0')})

union_test = odd_number_of_ones.union(even_length)
union_test_manual = DFA('union_test_manual', binary,
						{('q0', 'q0'), ('q0', 'q1'), ('q1', 'q0'), ('q1', 'q1')}, ('q0', 'q0'),
						{
							('q0', 'q0'): {Char('0'): ('q0', 'q1'), Char('1'): ('q1', 'q1')},
							('q0', 'q1'): {Char('0'): ('q0', 'q0'), Char('1'): ('q1', 'q0')},
							('q1', 'q0'): {Char('0'): ('q1', 'q1'), Char('1'): ('q0', 'q1')},
							('q1', 'q1'): {Char('0'): ('q1', 'q0'), Char('1'): ('q0', 'q0')}
						},
						{('q0', 'q0'), ('q1', 'q0'), ('q1', 'q1')})

nfa_n1 = NFA('nfa_n1', binary,
			{'q1', 'q2', 'q3', 'q4', 'q5'}, 'q1',
			{
				'q1': {Char('0'): ['q1'], Char('1'): ['q1', 'q2']},
				'q2': {Char('0'): ['q3'], Char('1'): ['q5'], 'ε': ['q3']},
				'q3': {Char('0'): ['q5'], Char('1'): ['q4']},
				'q4': {Char('0'): ['q4'], Char('1'): ['q4']},
				'q5': {Char('0'): ['q5'], Char('1'): ['q5']}
			},
			{'q4'})

nfa_n2 = NFA('nfa_n2', binary,
			{'q1', 'q2', 'q3', 'q4', 'q5'}, 'q1',
			{
				'q1': {Char('0'): ['q1'], Char('1'): ['q1', 'q2']},
				'q2': {Char('0'): ['q3'], Char('1'): ['q3']},
				'q3': {Char('0'): ['q4'], Char('1'): ['q4']},
				'q4': {Char('0'): ['q5'], Char('1'): ['q5']},
				'q5': {Char('0'): ['q5'], Char('1'): ['q5']}
			},
			{'q4'})

nfa_n3 = NFA('nfa_n3', Alphabet([Char('0')]),
			{'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}, 'q0',
			{
				'q0': {Char('0'): ['q6'], 'ε': ['q1', 'q3']},
				'q1': {Char('0'): ['q2']},
				'q2': {Char('0'): ['q1']},
				'q3': {Char('0'): ['q4']},
				'q4': {Char('0'): ['q5']},
				'q5': {Char('0'): ['q3']},
				'q6': {Char('0'): ['q6']}
			},
			{'q1', 'q3'})

nfa_n4 = NFA('nfa_n4', Alphabet([Char('a'), Char('b')]),
			{'q1', 'q2', 'q3', 'q4'}, 'q1',
			{
				'q1': {Char('a'): ['q4'], Char('b'): ['q2'], 'ε': ['q3']},
				'q2': {Char('a'): ['q2', 'q3'], Char('b'): ['q3']},
				'q3': {Char('a'): ['q1'], Char('b'): ['q4']},
				'q4': {Char('a'): ['q4'], Char('b'): ['q4']}
			},
			{'q1'})

n3_concat_n4 = nfa_n3.concat(nfa_n4)

n3_kleene = nfa_n3.kleene()

if __name__ == '__main__':
	# Test DFA that does not accept anything
	test_cases = [([], False), ('1', False), ('00', False), ('01', False), ('10', False), ('11', False), ('000', False), ('001', False), ('010', False), ('011', False), ('0000', False), ('1111', False)]
	run_dfa_tests(no_strings, test_cases)

	# Test DFA that accepts even length strings
	test_cases = [([], True), ('0', False), ('1', False), ('00', True), ('01', True), ('10', True), ('11', True), ('000', False), ('001', False), ('010', False), ('011', False), ('0000', True)]
	run_dfa_tests(even_length, test_cases)

	# Test DFA that accepts only one character
	test_cases = [([], False), ('0', True), ('1', True), ('00', False), ('01', False), ('10', False), ('11', False), ('000', False), ('001', False), ('010', False), ('011', False), ('0000', False)]
	run_dfa_tests(only_one_char, test_cases)

	# Test DFA that accepts the empty string
	test_cases = [([], True), ('1', False), ('00', False), ('01', False), ('10', False), ('11', False), ('000', False), ('001', False), ('010', False), ('011', False), ('0000', False), ('1111', False)]
	run_dfa_tests(empty_string, test_cases)

	# Test DFA that accepts odd length strings
	test_cases = [([], False), ('0', True), ('1', True), ('00', False), ('01', False), ('10', False), ('11', False), ('000', True), ('001', True), ('010', True), ('011', True), ('0000', False)]
	run_dfa_tests(odd_length, test_cases)

	# Test DFA that accepts even binary numbers
	test_cases = [([], False), ('0', True), ('1', False), ('00', True), ('01', False), ('10', True), ('11', False), ('000', True), ('001', False), ('010', True), ('011', False), ('1110', True)]
	run_dfa_tests(even_binary, test_cases)

	test_cases = [([], True), ('0', False), ('1', True), ('00', False), ('01', True), ('10', False), ('11', True), ('000', False), ('001', True), ('010', False), ('011', True), ('1110', False)]
	run_dfa_tests(even_binary.complement(), test_cases)

	# Test DFA that accepts odd binary numbers
	test_cases = [([], False), ('0', False), ('1', True), ('00', False), ('01', True), ('10', False), ('11', True), ('000', False), ('001', True), ('010', False), ('011', True), ('1011', True)]
	run_dfa_tests(odd_binary, test_cases)

	# Test DFA that accepts strings with some consecutive zeros
	test_cases = [([], False), ('0', False), ('1', False), ('00', True), ('01', False), ('10', False), ('11', False), ('000', True), ('001', True), ('0000', True), ('0100', True), ('010010', True)]
	run_dfa_tests(consecutive_zeros, test_cases)

	# Test DFA that accepts strings with some consecutive ones
	test_cases = [([], False), ('0', False), ('1', False), ('11', True), ('10', False), ('01', False), ('00', False), ('111', True), ('110', True), ('1111', True), ('1011', True), ('101101', True)]
	run_dfa_tests(consecutive_ones, test_cases)

	# Test DFA that accepts a string that contains 001 in it
	test_cases = [([], False), ('0', False), ('1', False), ('11', False), ('10', False), ('01', False), ('001', True), ('1001', True), ('0001', True), ('11001', True), ('0011', True), ('000111', True)]
	run_dfa_tests(contains_001, test_cases)

	# Test DFA that accepts strings of only ones
	test_cases = [([], False), ('0', False), ('01', False), ('00', False), ('000', False), ('001', False), ('1', True), ('11', True), ('111', True), ('1111', True), ('11111', True), ('111111', True)]
	run_dfa_tests(only_ones, test_cases)

	# Test DFA that accepts strings of only zeros
	test_cases = [([], False), ('1', False), ('10', False), ('11', False), ('111', False), ('110', False), ('0', True), ('00', True), ('000', True), ('0000', True), ('00000', True), ('000000', True)]
	run_dfa_tests(only_zeros, test_cases)

	# Test DFA that accepts my name 'dave'
	test_cases = [([], False), ('dave', True), ('jay', False), ('evad', False), ('daved', False), ('d', False), ('a', False), ('v', False), ('e', False), ('#dave', False), ('', False), ('#', False)]
	run_dfa_tests(dave, test_cases) # We can only have one accepting string so I can't show 6 different passes

	# Test DFA that starts with '#' to signify a comment
	test_cases = [([], False), ('#', True), ('#dave', True), ('#jay', True), ('##', True), ('#dave#', True), ('#"jay"', True), ('dave', False), ('jay', False), ('dave#', False), ('jay##', False), ('', False)]
	run_dfa_tests(comment, test_cases)

	# Test DFA that accepts valid strings that start and end with a double qoute
	test_cases = [([], False), ('""""', False), ('"', False), ('d"dave"', False), ('"jay"j', False), ('dave"', False), ('""', True), ('"dave"', True), ('"jay"', True), ('"#"', True), ('"#dave"', True), ('"e"', True)]
	run_dfa_tests(valid_string, test_cases)

	# Test DFA that accepts strings that have a zero
	test_cases = [([], False), ('0', True), ('01', True), ('00', True), ('000', True), ('001', True), ('010', True), ('11', False), ('111', False), ('1111', False), ('11111', False), ('111111', False)]
	run_dfa_tests(has_a_zero, test_cases)

	# Test DFA that accepts strings accepted by either consecutive_ones or contains_001
	test_cases = [([], False), ('0', False), ('01', False), ('11', True), ('111', True), ('110', True), ('010', False), ('0011', True), ('0001', True), ('00011', True), ('0000', False), ('01000', False)]
	run_dfa_tests(consecutive_ones_or_contains_001, test_cases)
	
	# Test DFA that accepts strings accepted by either even_length or only_ones
	test_cases = [([], True), ('0', False), ('01', True), ('00', True), ('000', False), ('001', False), ('010', False), ('101', False), ('111', True), ('1111', True), ('11111', True), ('111111', True)]
	run_dfa_tests(even_length_or_only_ones, test_cases)

	# Test DFA that accepts strings accepted by either consecutive_ones and contains_001
	test_cases = [([], False), ('0', False), ('01', False), ('11', False), ('111', False), ('110', False), ('0011', True), ('10011', True), ('00011', True), ('11001', True), ('111001', True), ('1001111', True)]
	run_dfa_tests(consecutive_ones_and_contains_001, test_cases)
	
	# Test DFA that accepts strings accepted by either even_length and only_ones
	test_cases = [([], False), ('0', False), ('01', False), ('00', False), ('000', False), ('001', False), ('11', True), ('1111', True), ('111111', True), ('11111111', True), ('1111111111', True), ('111111111111', True)]
	run_dfa_tests(even_length_and_only_ones, test_cases)

	# Test if contains_001 is a subset of each test DFA
	test_cases = [(contains_001, True), (consecutive_ones_or_contains_001, True), (consecutive_ones_and_contains_001, False)]
	run_dfa_subset_tests(contains_001, test_cases)

	# Test if consecutive_zeros is a subset of each test DFA
	test_cases = [(consecutive_zeros, True), (consecutive_ones_or_contains_001, False), (consecutive_ones_and_contains_001, False), (contains_001, False)]
	run_dfa_subset_tests(consecutive_zeros, test_cases)

	# Test if consecutive_zeros is a subset of each test DFA
	test_cases = [(even_length, True), (consecutive_ones_or_contains_001, False), (consecutive_ones_and_contains_001, False)]
	run_dfa_subset_tests(even_length, test_cases)

	# Test if only_zeros is a subset of each test DFA
	test_cases = [(only_zeros, True), (odd_length, False), (consecutive_zeros, False)]
	run_dfa_subset_tests(only_zeros, test_cases)

	# Test if only_zeros is equal to each test DFA
	test_cases = [(only_zeros, True), (only_ones, False), (~(only_zeros), False), (~(~(only_zeros)), True)]
	run_dfa_equality_tests(only_zeros, test_cases)

	# Test if consecutive_ones_or_contains_001 is equal to each test DFA
	test_cases = [(consecutive_ones_or_contains_001, True), (only_ones, False), (~(consecutive_ones_or_contains_001), False), (~(~(consecutive_ones_or_contains_001)), True)]
	run_dfa_equality_tests(consecutive_ones_or_contains_001, test_cases)

	# Test if consecutive_ones_and_contains_001 is equal to each test DFA
	test_cases = [(consecutive_ones_and_contains_001, True), (only_ones, False), (~(consecutive_ones_and_contains_001), False), (consecutive_ones_or_contains_001, False)]
	run_dfa_equality_tests(consecutive_ones_and_contains_001, test_cases)

	# Test if intersect and equality functions work
	test_cases = [(intersect_test, True), (intersect_test_manual, True), (odd_number_of_ones.union(even_length), False)]
	run_dfa_equality_tests(intersect_test, test_cases)

	# Test if union and equality functions work
	test_cases = [(union_test, True), (union_test_manual, True), (odd_number_of_ones.intersect(even_length), False)]
	run_dfa_equality_tests(union_test, test_cases)

	# Test nfa_n1 traces [(Char(), Next State), ...]
	test_cases = [
		([(Char('0'), 'q1'), (Char('1'), 'q2'), (Char('0'), 'q3'), (Char('1'), 'q4'), (Char('1'), 'q4'), (Char('0'), 'q4')], True),
		([(Char('1'), 'q1'), (Char('0'), 'q1'), (Char('1'), 'q2'), (Char('0'), 'q3'), (Char('1'), 'q4')], True),
		([(Char('1'), 'q2'), (Char(), 'q3'), (Char('1'), 'q4')], True)
	]
	run_nfa_oracle_test(nfa_n1, test_cases)

	# Test nfa_n2 traces, 1 in the third position from the end
	test_cases = [
		([(Char('0'), 'q1'), (Char('0'), 'q1'), (Char('0'), 'q1'), (Char('1'), 'q2'), (Char('0'), 'q3'), (Char('0'), 'q4')], True),
		([(Char('0'), 'q1'), (Char('0'), 'q1'), (Char('1'), 'q2'), (Char('0'), 'q3'), (Char('0'), 'q4'), (Char('0'), 'q5')], False),
		([(Char('1'), 'q2'), (Char('0'), 'q3'), (Char('0'), 'q4')], True)
	]
	run_nfa_oracle_test(nfa_n2, test_cases)

	# Test nfa_n3 traces, all strings of the form 0^k where k is a multiple of 2 or 3
	test_cases = [
		([(Char(), 'q1')], True),
		([(Char(), 'q1'), (Char('0'), 'q2'), (Char('0'), 'q1')], True),
		([(Char(), 'q3'), (Char('0'), 'q4'), (Char('0'), 'q5'), (Char('0'), 'q3')], True),
		([(Char(), 'q3'), (Char('0'), 'q4'), (Char('0'), 'q5'), (Char('0'), 'q3'), (Char('0'), 'q4'), (Char('0'), 'q5')], False)
	]
	run_nfa_oracle_test(nfa_n3, test_cases)

	# Test nfa_n4 traces [(Char(), Next State), ...]
	test_cases = [
		([(Char(), 'q3'), (Char('a'), 'q1'), (Char('b'), 'q2'), (Char('b'), 'q3')], False),
		([(Char('b'), 'q2'), (Char('a'), 'q2'), (Char('b'), 'q3'), (Char('a'), 'q1')], True),
		([(Char(), 'q3'), (Char('a'), 'q1')], True)
	]
	run_nfa_oracle_test(nfa_n4, test_cases)

	# Test concat of nfa_n3 and nfa_n4
	test_cases = [([], True), ('0', False), ('00', True), ('000', True), ('00000', False), ('00b', False), ('00baa', True), ('000a', True), ('baaba', True), ('ba', False), ('00bb', False), ('000bbab', False)]
	run_dfa_tests(n3_concat_n4, test_cases)

	# Test kleene star nfa_n3, every True example is something that would not be accepted orignally by n3 (0* length is prime)
	test_cases = [('0', False), ('00000', True), ('0000000', True), ('00000000000', True), ('0000000000000', True), ('00000000000000000', True)]
	run_dfa_tests(n3_kleene, test_cases)
	