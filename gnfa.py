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

def sequence(literals):
	def gh(r):
		if isinstance(r, regex):
			return r
		#print('asd', type(r))
		return re_c(r)

	if len(literals) == 1:
		#print('asdasd', literals[0], type(literals[0]))
		if literals[0] == 'ε':
			return re_eps()
		gdsa = gh(literals[0])
		print(1, type(gdsa))
		return gdsa


	def fh(i):
		if i < len(literals):
			if not fh(i + 1):
				if type(literals[i]) == re_eps:
					return re_eps()
				return gh(literals[i])
			if type(literals[i]) == re_eps:
				return re_u(re_eps(), fh(i + 1))
			return re_u(gh(literals[i]), fh(i + 1))

	r = fh(0)
	return r

def alternation(literals):
	def gh(r):
		if isinstance(r, regex):

			return r
		#print('asd', type(r))
		print('asddd', r)
		return re_c(r)

	if len(literals) == 1:
		#print('asdasd', literals[0], type(literals[0]))
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
	@classmethod
	def from_dfa(cls, dfa):
		delta = {}

				# remove un-needed states/ transitions like the hell state
		if 'Hell' in dfa.δ:
			dfa.δ.pop('Hell')
		for qi, t in dfa.δ.items():
			for c, tr in list(t.items()):
				if tr == 'Hell':
					t.pop(c)

		for s in dfa.δ:
			s_delta = {}
			for next_s, xs in next_states(dfa, s).items():
				literals = [re_c(x) for x in xs]
				#print('alternation:', alternation(literals))
				s_delta[next_s] = alternation(literals)
			delta[s] = s_delta
		init_delta = {}
		init_delta[dfa.q0] = re_eps()
		delta['g0'] = init_delta
		#delta['g1'] = {}
		for accept_state in dfa.F:
			delta[accept_state]['g1'] = re_eps()

		pprint(delta)

		return GNFA(dfa.name, dfa.Q, 'g0', delta, {'g1'})

	def arbitrary_state(self):
		for s in self.δ.keys():
			if s != self.q0:
				return s
		return None

	def incoming_edges(self, next_s):
		edges = []
		for s, s_delta in self.δ.items():
			if next_s in s_delta:
				edges.append((s, s_delta[next_s]))
		return edges

	def outgoing_edges(self, s):
		edges = []
		for next_s, r_out in self.δ[s].items():
			edges.append((next_s, r_out))
		return edges

	def delete_state(self, s):
		del self.δ[s]
		for s_delta in self.δ.values():
			if s in s_delta:
				del s_delta[s]

	def loop_regex(self, s):
		return self.transition(s, s)

	def transition(self, s, next_s):
		return self.δ[s].get(next_s, re_eps())

	def rip_state(self, q_rip):
		in_list = self.incoming_edges(q_rip)
		out_list = self.outgoing_edges(q_rip)
		R_rip = re_star(self.loop_regex(q_rip))

		for q_in, r_in in in_list:
			for q_out, r_out in out_list:
				r_rip_replacement = sequence([r_in, R_rip, r_out])
				old_in_out = self.transition(q_in, q_out)
				self.δ[q_in][q_out] = alternation([old_in_out, r_rip_replacement])

		self.delete_state(q_rip)

	def rip_all(self):
		q_rip = self.arbitrary_state()
		
		while q_rip is not None:
			#print(q_rip)
			self.rip_state(q_rip)
			q_rip = self.arbitrary_state()


	@classmethod
	def dfa_re(cls, dfa):
		m = cls.from_dfa(dfa)
		m.rip_all()
#		print(m)
		r = m.transition(m.q0, 'g1')
#		print(2, r)
		return r


	def from_dfa_old(self, dfa):
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

		for qi, t in δ.items():
			for c, tr in t.items():
				print(qi, ':', c, '\t=>', tr)
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