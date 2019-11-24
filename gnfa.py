from nfa import NFA
from regex import *
from pprint import pprint
class GNFA():
	def __init__(self, name, Σ, Q, q0, δ, F):
		self.name = name
		self.Σ = Σ
		self.Q = Q
		self.q0 = q0
		self.δ = δ
		self.F = F

	def from_dfa(self, dfa):
		nfa = NFA.from_dfa(dfa.name, dfa)
		Q = nfa.Q
		Q.update(['g0', 'g1'])
		δ = nfa.δ
		q0 = 'g0'
		F = {'g1'}

		δ['g0'] = {}
		δ['g1'] = {}
		δ['g0']['ε'] = [nfa.q0]
		newdelt = {}
		for qi in nfa.F:
			if not δ[qi].get('ε'):
				δ[qi]['ε'] = []
			δ[qi]['ε'].append('g1')

		yeah = {}
		for qi, s in δ.items():
			'''
				for each state check if the c have shared end states
			'''
		#	print(qi, t)
			yeah[qi] = {}
			for c, t in s.items():
				t = t.pop()
				if t not in yeah[qi]:
					yeah[qi][t] = []
				yeah[qi][t].append(c)
			
		pprint(yeah)
		#yeah['Hell']
		for k, v in yeah.items():
			newdelt[k] = {}
			for t, qi in v.items():
				def fh(i):
					if i < len(qi):
						if not fh(i + 1):
							if qi[i] == 'ε':
								return re_eps()
							return re_c(qi[i])
						if qi[i] == 'ε':
							return re_u(re_eps(), fh(i + 1))
						return re_u(re_c(qi[i]), fh(i + 1))
					return 0

				r = fh(0)
				r.optimize()
				newdelt[k][r] = [t] #(t, qi)
		pprint(yeah)

		for k, v in newdelt.items():
			d = False
			for q in v:
				if type(q) == re_null:
					d = True
					break
			if not d:
				v[re_null()] = []
			if k != 'g1':
				for q in Q:
					if q not in v.values():
						if q != 'g0':
							e_state = None
							for qd in v:
								if type(qd) == re_null:
									e_state = qd
									break
							#print(q, v)
							print(type(qd))
							if q not in v[qd] and q not in yeah[k]:
								v[qd].append(q)

		pprint(newdelt)
		return None

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