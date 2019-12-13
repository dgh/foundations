from nfa import NFA
from regex import *
from copy import deepcopy
from pprint import pprint

class GNFA():
	def __init__(self, name, Q, q0, δ, F):
		self.name = name
		self.Q = Q
		self.q0 = q0
		self.δ = δ
		self.F = F

	@classmethod
	def from_dfa(cls, dfa):
		# return an GNFA
		delta = deepcopy(dfa.δ)

		if 'Hell' in delta:
			delta.pop('Hell')
		for qi, t in delta.items():
			for c, tr in list(t.items()):
				if tr == 'Hell':
					t.pop(c)

		pprint(dfa.δ)
		pprint(delta)

		return GNFA(dfa.name, dfa.Q, 'g0', delta, {'g1'})

	@classmethod
	def dfa_re(cls, dfa):
		#return regex
		pass

{'qA', 'qB', 'qC'}, 'qA'
{
	'qA': {Char('0'): ['qB'], Char('1'): ['qA']},
	'qB': {Char('0'): ['qB'], Char('1'): ['qC']},
	'qC': {Char('0'): ['qC'], Char('1'): ['qC']},
}, {'qC'}

{'g0', 'qA', 'qB', 'qC', 'g1'}, 'g0'
{
	'g0': {'ε': ['qA']},
	'qA': {Char('0'): ['qB'], Char('1'): ['qA']},
	'qB': {Char('0'): ['qB'], Char('1'): ['qC']},
	'qC': {Char('0'): ['qC'], Char('1'): ['qC'], 'ε': ['g1']},
	'g1': {}
}, 'g1'

{'g0', 'qA', 'qB', 'qC', 'g1'}, 'g0'
{
	'g0': {'ε': ['qA']},
	'qA': {Char('0'): ['qB'], Char('1'): ['qA']},
	'qB': {Char('0'): ['qB'], Char('1'): ['qC']},
	'qC': {re_u('0', '1'): ['qC'], 'ε': ['g1']},
	'g1': {}
}, 'g1'