import math
from itertools import product
from char import Char
from alphabet import Alphabet
from string import String
from dfa import DFA

def generate_nth_string(a, n):
	if not n: return String([Char()], a)
	# |A|^l
	l = int(math.log(n + 1, len(a))) # l = layer
	i =  n + 1 - len(a) ** l # i = layer index + 1
	return String(list(product(a, repeat=l))[i], a)
	
def test_dfa(d, s, expected):
	if d.accepts(s) != expected:
		print(f'Test of {d.name} FAILED with {s}, expected {expected} but got {not expected}!')
		return False
	return True

def run_dfa_tests(d, tests):
	passed = 0
	for test in tests:
		if test_dfa(d, String(test[0], d.Σ), test[1]):
			passed += 1
	print(f'{passed}/{len(tests)} tests PASSED for {d.name}!')
	return passed

binary = Alphabet([Char('0'), Char('1')])
alpha = Alphabet([Char(c) for c in 'abcdefghijklmnopqrstuvwxyz#"'])

no_strings_dfa = DFA('no_strings_dfa', binary,
					 (lambda qi: False), 0,
					 (lambda qi, c: False),
					 (lambda qi: False))

empty_string_dfa = DFA('empty_string_dfa', binary,
					   (lambda qi: qi == 0 or qi == 1), 0,
					   (lambda qi, c: 1 if c else 0),
					   (lambda qi: qi == 0))

only_one_char_dfa = DFA('only_one_char_dfa', binary,
						(lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
						(lambda qi, c: 1 if qi == 0 and c else 2),
						(lambda qi: qi == 1))

even_length_dfa = DFA('even_length_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if qi == 0 and c else 0),
					  (lambda qi: qi == 0))

odd_length_dfa = DFA('odd_length_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if qi == 0 and c else 0),
					  (lambda qi: qi == 1))

even_binary_dfa = DFA('even_binary_dfa', binary,
					  (lambda qi: qi == 0 or qi == 1), 0,
					  (lambda qi, c: 1 if c == '0' else 0),
					  (lambda qi: qi == 1))

odd_binary_dfa = DFA('odd_binary_dfa', binary,
					 (lambda qi: qi == 0 or qi == 1), 0,
					 (lambda qi, c: 0 if c == '0' else 1),
					 (lambda qi: qi == 1))

dave_dfa = DFA('dave_dfa', alpha,
			   (lambda qi: qi == 0 or qi == 1 or qi == 2 or qi == 3 or qi == 4 or qi == 5), 0,
			   (lambda qi, c: 1 if qi == 0 and c == 'd' else 2 if qi == 1 and c == 'a' else 3 if qi == 2 and c == 'v' else 4 if qi == 3 and c == 'e' else 5),
			   (lambda qi: qi == 4))

python_comment_dfa = DFA('python_comment_dfa', alpha,
 						 (lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
						 (lambda qi, c: 1 if qi == 0 and c == '#' else 1 if qi == 1 else 2),
						 (lambda qi: qi == 1))

consecutive_zeros_dfa = DFA('consecutive_zeros_dfa', binary,
							(lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
							(lambda qi, c: 1 if qi == 0 and c == '0' else 2 if qi == 1 and c == '0' else 2 if qi == 2 else 0),
							(lambda qi: qi == 2))

consecutive_ones_dfa = DFA('consecutive_ones_dfa', binary,
						   (lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
						   (lambda qi, c: 1 if qi == 0 and c == '1' else 2 if qi == 1 and c == '1' else 2 if qi == 2 else 0),
						   (lambda qi: qi == 2))

valid_string_dfa = DFA('valid_string_dfa', alpha,
					   (lambda qi: qi == 0 or qi == 1 or qi == 2 or qi == 3 or qi == 4), 0,
					   (lambda qi, c: 1 if qi == 0 and c == '"' else 2 if qi == 1 and c != '"' else 3 if qi == 2 and c == '"' else 3 if qi == 1 and c == '"' else 2 if qi == 2 else 4),
					   (lambda qi: qi == 3))

contains_001_dfa = DFA('contains_001_dfa', binary,
					   (lambda qi: qi == 0 or qi == 1 or qi == 2 or qi == 3), 0,
					   (lambda qi, c: 0 if qi == 0 and c == '1' else 1 if qi == 0 and c == '0' else 0 if qi == 1 and c == '1' else 2 if qi == 1 and c == '0' else 2 if qi == 2 and c == '0' else 3),
					   (lambda qi: qi == 3))

only_ones_dfa = DFA('only_ones_dfa', binary,
					(lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
					(lambda qi, c: 1 if qi != 2 and c == '1' else 2),
					(lambda qi: qi == 1))

only_zeros_dfa = DFA('only_zeros_dfa', binary,
					 (lambda qi: qi == 0 or qi == 1 or qi == 2), 0,
					 (lambda qi, c: 1 if qi != 2 and c == '0' else 2),
					 (lambda qi: qi == 1))

# Test DFA that accepts even length strings
tests = [([], True), ('0', False), ('1', False), ('00', True), ('01', True), ('10', True), ('11', True), ('000', False), ('001', False), ('010', False), ('011', False), ('0000', True)]
run_dfa_tests(even_length_dfa, tests)

# Test DFA that accepts odd length strings
tests = [([], False), ('0', True), ('1', True), ('00', False), ('01', False), ('10', False), ('11', False), ('000', True), ('001', True), ('010', True), ('011', True), ('0000', False)]
run_dfa_tests(odd_length_dfa, tests)

# Test DFA that accepts even binary numbers
tests = [([], False), ('0', True), ('1', False), ('00', True), ('01', False), ('10', True), ('11', False), ('000', True), ('001', False), ('010', True), ('011', False), ('1110', True)]
run_dfa_tests(even_binary_dfa, tests)

# Test DFA that accepts odd binary numbers
tests = [([], False), ('0', False), ('1', True), ('00', False), ('01', True), ('10', False), ('11', True), ('000', False), ('001', True), ('010', False), ('011', True), ('1011', True)]
run_dfa_tests(odd_binary_dfa, tests)

# Test DFA that accepts my name 'dave'
tests = [([], False), ('dave', True), ('jay', False), ('evad', False), ('daved', False), ('d', False), ('a', False), ('v', False), ('e', False), ('ddave', False), ('', False), ('g', False)]
run_dfa_tests(dave_dfa, tests) # We can only have one accepting string so I can't show 6 different passes

# Test DFA that starts with '#' to signify a comment
tests = [([], False), ('#', True), ('#comment', True), ('##', True), ('###', True), ('#comment#', True), ('#comment#comment#', True), ('dave', False), ('jay', False), ('comment#', False), ('comment##', False), ('', False)]
run_dfa_tests(python_comment_dfa, tests)

# Test DFA that accepts valid strings that start and end with a double qoute
tests = [([], False), ('""""', False), ('"', False), ('f"string"', False), ('"string"f', False), ('string"', False), ('""', True), ('"dave"', True), ('"jay"', True), ('"string"', True), ('"#comment"', True), ('"e"', True)]
run_dfa_tests(valid_string_dfa, tests)

# Test DFA that accepts strings with some consecutive zeros
tests = [([], False), ('0', False), ('1', False), ('00', True), ('01', False), ('10', False), ('11', False), ('000', True), ('001', True), ('0000', True), ('0100', True), ('010010', True)]
run_dfa_tests(consecutive_zeros_dfa, tests)

# Test DFA that accepts strings with some consecutive ones
tests = [([], False), ('0', False), ('1', False), ('11', True), ('10', False), ('01', False), ('00', False), ('111', True), ('110', True), ('1111', True), ('1011', True), ('101101', True)]
run_dfa_tests(consecutive_ones_dfa, tests)

# Test DFA that accepts a string that contains 001 in it
tests = [([], False), ('0', False), ('1', False), ('11', False), ('10', False), ('01', False), ('001', True), ('1001', True), ('0001', True), ('11001', True), ('0011', True), ('000111', True)]
run_dfa_tests(contains_001_dfa, tests)

# Test DFA that accepts strings of only ones
tests = [([], False), ('0', False), ('01', False), ('00', False), ('000', False), ('001', False), ('1', True), ('11', True), ('111', True), ('1111', True), ('11111', True), ('111111', True)]
run_dfa_tests(only_ones_dfa, tests)

tests = [([], False), ('1', False), ('10', False), ('11', False), ('111', False), ('110', False), ('0', True), ('00', True), ('000', True), ('0000', True), ('00000', True), ('000000', True)]
run_dfa_tests(only_zeros_dfa, tests)