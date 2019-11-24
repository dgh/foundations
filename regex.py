from char import Char
from string import String
from nfa import NFA

def regex_generate(r):
	return String(r.generate())

def regex_to_nfa(r, name, a):
	return NFA(name, a, *r.nfa())

def regex_optimize(r):
	return r.optimize()

class regex():
	def __repr__(self):
		return ''

	def generate(self):
		return ''

	def optimize(self):
		return self

class re_null(regex):
	def __init__(self):
		pass

	def __repr__(self):
		return '∅'

class re_eps(regex):
	def __init__(self):
		pass

	def nfa(self):
		Q = set(['0', '1'])
		q0 = '0'
		δ = {'0': {'ε': ['1']}, '1': {}}
		F = set(['1'])

		return Q, q0, δ, F

	def __repr__(self):
		return 'ε'

class re_c(regex):
	def __init__(self, c):
		if isinstance(c, str):
			c = Char(c)
		self.c = c

	def generate(self):
		return f'{self.c}'

	def nfa(self):
		Q = set(['0', '1'])
		q0 = '0'
		δ = {'0': {self.c: ['1']}, '1': {}}
		F = set(['1'])

		return Q, q0, δ, F

	def __repr__(self):
		return self.c.__repr__()

class re_u(regex):
	def __init__(self, lc, rc):
		self.l = lc
		self.r = rc

	def generate(self):
		return self.l.generate()

	def nfa(self):
		l_nfa = self.l.nfa()
		r_nfa = self.r.nfa()

		Q = l_nfa[0] # start with the states in lhs
		q0 = str(len(l_nfa[0]) + len(r_nfa[0])) # we're adding a new node so reserve the q0 to be the last one
		F = l_nfa[3] # start with the accepting in lhs

		'''
			Go through rhs δ and see if the state is already in Q
			if it is then its conflicting and we have to update it with a new state
			increment each character in rhs delta by the size of Q (lhs Q)
		'''
		δ = {}
		for qi, transitions in r_nfa[2].items(): # create a new delta with the updates state names for the rhs
			new_state = str(int(qi) + len(Q))
			δ[new_state] = dict()
			for c, states in transitions.items():
				δ[new_state][c] = [str(int(a) + len(Q)) for a in states]

		δ.update(l_nfa[2]) # add the original lhs delta back
		
		δ[q0] = {'ε': [l_nfa[1], str(int(r_nfa[1]) + len(Q))]}

		F.update([str(int(qi) + len(Q)) for qi in r_nfa[3]])

		for qi in δ.keys(): # Make sure the Q has the update rhs states
			Q.update(qi)

		return Q, q0, δ, F

	def optimize(self):
		if isinstance(self.l, re_eps) and isinstance(self.r, re_eps):
			self.__class__ = self.l.__class__

	def __repr__(self):
		return f'{self.l}∪{self.r}'

class re_cat(regex):
	def __init__(self, lc, rc):
		self.l = lc
		self.r = rc

	def generate(self):
		return f'{self.l.generate()}{self.r.generate()}'

	def nfa(self):
		l_nfa = self.l.nfa()
		r_nfa = self.r.nfa()

		Q = l_nfa[0] # set first to be the states in lhs
		q0 = l_nfa[1] # set to be the initial state in the lhs
		
		'''
			Go through rhs δ and see if the state is already in Q
			if it is then its conflicting and we have to update it with a new state
			increment each character in rhs delta by the size of Q (lhs Q)
		'''
		δ = {}
		for qi, transitions in r_nfa[2].items(): # create a new delta with the updates state names for the rhs
			new_state = str(int(qi) + len(Q))
			δ[new_state] = dict()
			for c, states in transitions.items():
				δ[new_state][c] = [str(int(a) + len(Q)) for a in states]

		δ.update(l_nfa[2]) # add the original lhs delta back

		for qi in l_nfa[3]: # Make the link between the accepting states in lhs and eps trans them to the initial state in rhs
			if not δ[qi].get('ε'):
				δ[qi]['ε'] = []
			δ[qi]['ε'].append(str(int(r_nfa[1]) + len(Q)))

		F = set([str(int(qi) + len(Q)) for qi in r_nfa[3]])

		for qi in δ.keys(): # Make sure the Q has the update rhs states
			Q.update(qi)

		return Q, q0, δ, F

	def optimize(self):
		if isinstance(self.l, re_null):
			self.__class__ = re_null
		elif isinstance(self.r, re_null):
			self.__class__ = re_null
		elif isinstance(self.l, re_eps):
			self.__class__ = self.r.__class__
		elif isinstance(self.r, re_eps):
			self.__class__ = self.l.__class__

	def __repr__(self):
		return f'{self.l}◦{self.r}'

class re_star(regex):
	def __init__(self, r):
		self.r = r

	def generate(self):
		return f'{self.r.generate()}'

	def nfa(self):
		r_nfa = self.r.nfa()

		Q = r_nfa[0]
		q0 = str(len(Q))
		δ = r_nfa[2]
		F = r_nfa[3]
		
		Q.add(q0)
		F.add(q0)
		δ[q0] = {}

		for qi in F:
			if not δ[qi].get('ε'):
				δ[qi]['ε'] = []
			δ[qi]['ε'].append(r_nfa[1])

		return Q, q0, δ, F

	def optimize(self):
		if isinstance(self.r, re_null):
			self.__class__ = re_eps

	def __repr__(self):
		return f'({self.r})*'
