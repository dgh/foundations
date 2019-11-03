from string import String
from alphabet import Alphabet
from itertools import product
from copy import deepcopy

class NFA():
	def __init__(self, name, Σ, Q, q0, δ, F):
		self.name = name
		self.Σ = Σ
		self.Q = Q
		self.q0 = q0
		self.δ = δ
		self.F = F

	def fromDFA(name, d):
		δ = dict()
		for state in d.δ:
			δ[state] = dict()
			for c in d.δ[state]:
				δ[state][c] = [d.δ[state][c]]

		return NFA(name, d.Σ, d.Q, d.q0, δ, d.F)

	def accepts(self, s):
		def epsilon_closure(qi):
			stack = []
			visited = set([qi])

			if self.δ[qi].get('ε'):
				stack.extend(self.δ[qi]['ε'])

			while stack:
				state = stack.pop()
				if state not in visited:
					visited.add(state)
					if self.δ[state].get('ε'):
						stack.extend(self.δ[state]['ε'])

			return visited

		states = epsilon_closure(self.q0)

		for c in s:
			if c.is_empty(): continue

			next_states = set()
			for qi in states:
				if self.δ[qi].get(c):
					for next_state in self.δ[qi][c]:
						next_states.update(epsilon_closure(next_state))

			states = next_states

		return True if (states & self.F) else False

	def oracle(self, s, trace, expected):
		if s != String(''.join(str(t[0]) for t in trace)):
			print(f'String<{s}> does not match the given trace for {self.name}!')
			return False

		qi = self.q0
		for t in trace:
			if t[1] in self.δ[qi].get(t[0]):
				qi = t[1]
			else:
				print(f'{trace} is not a valid trace for {self.name}!')
				return False

		return self.accepts(s) == expected

	def cross(self, other, cond, name):
		states = set()
		accepts = set()
		delta = dict()

		for qi1 in self.Q:
			for qi2 in other.Q:
				states.add((qi1, qi2))
				delta[(qi1, qi2)] = dict()
				for c in self.Σ:
					delta[(qi1, qi2)][c] = list(product(self.δ[qi1][c], other.δ[qi2][c]))
					
		for (qi1, qi2) in states:
			if cond(qi1 in self.F, qi2 in other.F):
				accepts.add((qi1, qi2))

		return NFA(name, self.Σ, states, (self.q0, other.q0), delta, accepts)

	def union(self, other):
		return self.cross(other, bool.__or__, f'{self.name}_or_{other.name}')

	def concat(self, other):
		name = self.name + '_concat_' + other.name
		Σ = Alphabet(set(self.Σ).union(other.Σ))
		Q = self.Q.union(set([other.name + '_' + s for s in other.Q]))
		δ = deepcopy(self.δ)
		q0 = self.q0
		F = set([other.name + '_' + s for s in other.F])

		nδ = {}
		for qi, transitions in other.δ.items():
			new_state = other.name + '_' + qi
			nδ[new_state] = dict()
			for c, states in transitions.items():
				nδ[new_state][c] = [other.name + '_' + a for a in states]

		δ.update(nδ)

		for qi in self.F:
			δ[qi]['ε'] = [other.name + '_' + other.q0] + (δ[qi].get('ε') or [])

		return NFA(name, Σ, Q, q0, δ, F)

	def kleene(self):
		name = self.name + '_kleene'
		Σ = self.Σ
		Q = self.Q.copy()
		δ = deepcopy(self.δ)
		q0 = 'k0'
		F = {'k0'}

		Q.add('k0')
		δ['k0'] = {'ε': list(F.union({self.q0}))}

		for qi in self.F:
			δ[qi]['ε'] = ['k0'] + (δ[qi].get('ε') or [])

		return NFA(name, Σ, Q, q0, δ, F)