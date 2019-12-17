from nfa import NFA
from regex import *
from copy import deepcopy
from pprint import pprint

def next_states(dfa, s):
	next_states = {}
	for x, next_s in dfa.δ[s].items():
		if next_s not in next_states:
			next_states[next_s] = []
		next_states[next_s].append(x)
	return next_states

def alternation(literals):
	def gh(r):
		if isinstance(r, regex):
			return r
		return re_c(r)

	if len(literals) == 1:
		if literals[0] == 'ε':
			return re_eps()
		return gh(literals[0])

	def fh(i):
		if i < len(literals):
			if not fh(i + 1):
				if type(literals[i]) == re_eps:
					return re_eps()
				return gh(literals[i])
			if type(literals[i]) == re_eps:
				return re_cat(re_eps(), fh(i + 1))
			return re_cat(gh(literals[i]), fh(i + 1))

	r = fh(0)
	return r

class GNFA():
	def __init__(self, name, Q, q0, δ, F):
		self.name = name
		self.Q = Q
		self.q0 = q0
		self.δ = δ
		self.F = F

	@classmethod
	def from_dfa(cls, dfa):
		delta = {}
		ddelta = deepcopy(dfa.δ)

		for s in ddelta:
			s_delta = {}
			for next_s, xs in next_states(dfa, s).items():
				literals = [re_c(x) for x in xs]
				s_delta[next_s] = alternation(literals)
			delta[s] = s_delta
		init_delta = {}
		init_delta[dfa.q0] = re_eps()
		delta['g0'] = init_delta
		delta['g1'] = {}
		for accept_state in dfa.F:
			delta[accept_state]['g1'] = re_eps()

		return GNFA(dfa.name, dfa.Q, 'g0', delta, 'g1')