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

	# def from_dfa(self, dfa):
	# 	nfa = NFA.from_dfa(dfa.name, dfa)
	# 	Q = nfa.Q
	# 	Q.update(['g0', 'g1'])
	# 	δ = nfa.δ
	# 	q0 = 'g0'
	# 	F = {'g1'}

	# 	δ['g0'] = {}
	# 	δ['g1'] = {}
	# 	δ['g0']['ε'] = [nfa.q0]
	# 	newdelt = {}
	# 	for qi in nfa.F:
	# 		if not δ[qi].get('ε'):
	# 			δ[qi]['ε'] = []
	# 		δ[qi]['ε'].append('g1')

	# 	yeah = {}
	# 	for qi, s in δ.items():
	# 		'''
	# 			for each state check if the c have shared end states
	# 		'''
	# 	#	print(qi, t)
	# 		yeah[qi] = {}
	# 		for c, t in s.items():
	# 			t = t.pop()
	# 			if t not in yeah[qi]:
	# 				yeah[qi][t] = []
	# 			yeah[qi][t].append(c)
			
	# 	pprint(yeah)
	# 	#yeah['Hell']
	# 	for k, v in yeah.items():
	# 		newdelt[k] = {}
	# 		for t, qi in v.items():
	# 			def fh(i):
	# 				if i < len(qi):
	# 					if not fh(i + 1):
	# 						if qi[i] == 'ε':
	# 							return re_eps()
	# 						return re_c(qi[i])
	# 					if qi[i] == 'ε':
	# 						return re_u(re_eps(), fh(i + 1))
	# 					return re_u(re_c(qi[i]), fh(i + 1))
	# 				return 0

	# 			r = fh(0)
	# 			r.optimize()
	# 			newdelt[k][r] = [t] #(t, qi)
	# 	pprint(yeah)

	# 	for k, v in newdelt.items():
	# 		d = False
	# 		for q in v:
	# 			if type(q) == re_null:
	# 				d = True
	# 				break
	# 		if not d:
	# 			v[re_null()] = []
	# 		if k != 'g1':
	# 			for q in Q:
	# 				if q not in v.values():
	# 					if q != 'g0':
	# 						e_state = None
	# 						for qd in v:
	# 							if type(qd) == re_null:
	# 								e_state = qd
	# 								break
	# 						#print(q, v)
	# 						print(type(qd))
	# 						if q not in v[qd] and q not in yeah[k]:
	# 							v[qd].append(q)

	# 	pprint(newdelt)
	# 	return None
	def from_dfa(self, dfa):
		nfa = NFA.from_dfa(dfa.name, dfa)
		name = nfa.name
		Q = nfa.Q.copy()
		q0 = 'g0'
		δ = deepcopy(nfa.δ)
		F = {'g1'}

		Q.update(['g0', 'g1'])
		δ.update({'g0': {'ε': [nfa.q0]}})
		δ.update({'g1': {}})

		# Add eps transitions from previous accept states to new gnfa accept state
		for qi in nfa.F:
			if not δ[qi].get('ε'):
				δ[qi]['ε'] = []
			δ[qi]['ε'].append('g1')

		# remove un-needed states/ transitions like the hell state
		if 'Hell' in δ:
			δ.pop('Hell')
		for qi, t in δ.items():
			for c, tr in list(t.items()):
				if 'Hell' in tr:
					tr.remove('Hell')
					if not tr:
						t.pop(c)

		# go through each state, if multiple char transition to the same state combine
		nδ = {}
		for qi, t in δ.items():
			nδ[qi] = {}
			test = {}
			for c, tr in t.items():
				tr = tr[0]
				if tr not in test:
					test[tr] = []
				test[tr].append(c)

			for l, q in test.items():
				def fh(i):
					if i < len(q):
						if not fh(i + 1):
							if q[i] == 'ε':
								return re_eps()
							return re_c(q[i])
						if q[i] == 'ε':
							return re_u(re_eps(), fh(i + 1))
						return re_u(re_c(q[i]), fh(i + 1))
					return 0
					
				r = fh(0)
				nδ[qi].update({r: [l]})

		δ = nδ

		# for qi, t in δ.items():
		# 	for c, tr in t.items():
		# 		print(qi, t)
		return GNFA(name, Q, q0, δ, F)

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