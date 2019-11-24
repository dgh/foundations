from char import Char
from string import String

class DFA():
	def __init__(self, name, Σ, Q, q0, δ, F):
		self.name = name
		self.Σ = Σ
		self.Q = Q
		self.q0 = q0
		self.δ = δ
		self.F = F

		if 'Hell' not in self.Q:
			self.Q.add('Hell')
			self.δ.update({'Hell':{}})

		for qi, v in self.δ.items():
			for c in self.Σ:
				if c not in v:
					v.update({c: 'Hell'})

	def accepts(self, s):
		qi = self.q0
		for c in s:
			if c.is_empty(): continue
			if not self.δ[qi].get(c): return False
			qi = self.δ[qi][c]

		return qi in self.F

	def get_accepted(self):
		visited = set()
		s = []
		
		def traverse(qi):
			if qi in self.F:
				return True
			elif qi in visited:
				return False

			visited.add(qi)

			for c in self.Σ:
				next_state = self.δ[qi][c]
				if traverse(next_state):
					s.insert(0, c)
					return True

			return False

		if self.q0 in self.F:
			return String([Char()])

		if traverse(self.q0):
			return String(s)

		return False

	def trace(self, s):
		states = []
		qi = self.q0
		for c in s:
			states.append(qi)
			qi =  self.δ[qi][c]
		return states

	def cross(self, other, cond, name):
		states = set()
		accepts = set()
		delta = dict()

		for qi1 in self.Q:
			for qi2 in other.Q:
				states.add((qi1, qi2))
				delta[(qi1, qi2)] = dict()
				for c in self.Σ:
					delta[(qi1, qi2)][c] = (self.δ[qi1][c], other.δ[qi2][c])

		for (qi1, qi2) in states:
			if cond(qi1 in self.F, qi2 in other.F):
				accepts.add((qi1, qi2))

		return DFA(name, self.Σ, states, (self.q0, other.q0), delta, accepts)

	def union(self, other):
		return self.cross(other, bool.__or__, f'{self.name}_or_{other.name}')

	def intersect(self, other):
		return self.cross(other, bool.__and__, f'{self.name}_and_{other.name}')

	def complement(self):
		return DFA(f'{self.name}_c', self.Σ, self.Q, self.q0, self.δ, self.Q - self.F)

	def subset(self, other):
		if self.intersect(other.complement()).get_accepted():
			return False
		return True

	def equal(self, other):
		return self.subset(other) and other.subset(self)

	def __contains__(self, other):
		return other.subset(self)

	def __eq__(self, other):
		return self in other and other in self

	def __invert__(self):
		return self.complement()