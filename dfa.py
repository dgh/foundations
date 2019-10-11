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

	def accepts(self, s):
		qi = self.q0
		for c in s:
			qi = self.δ[qi][c]

		return qi in self.F

	def get_accepted(self):
		'''
			problem: we cant return no string, just the empty string
			solution: be able to return nothing if nothing is acceptable
						and return empty string if q0 is accepting
						empty string ~= nothing
						0 ~= null
		'''
		visited = set()
		#dictionary = dict() # (A, C): '1' (C, D): '0'
		s = []
		def accept(qi):
			if qi in self.F:
				return True
			elif qi in visited:
				return False

			visited.add(qi)

			for c in self.Σ:
				next_state = self.δ[qi][c];
				if accept(next_state):
					#dictionary[(qi, next_state)] = c
					s.insert(0, c)
					return True
			return False

		if self.q0 in self.F:
			''' return empty'''
			return True

		accept(self.q0)
		
		return s


	def trace(self, s):
		states = []
		if self.accepts(s):
			qi = self.q0
			for c in s:
				states.append(qi)
				qi =  self.δ[qi][c]
			return states

		return False

	# def cross(self, other, cond, name):
	# 	states = set()
	# 	accepts = set()
	# 	delta = dict()

	# 	for qi1 in self.Q:
	# 		for qi2 in other.Q:
	# 			states.add((qi1, qi2))
	# 			delta[(qi1, qi2)] = dict()
	# 			for c in self.Σ:
	# 				delta[(qi1, qi2)][c] = (self.δ[qi1][c], other.δ[qi2][c])

	# 	for (qi1, qi2) in states:
	# 		if cond(qi1 in self.F, qi2 in other.F):
	# 			accepts.add((qi1, qi2))

	# 	return DFA(name, self.Σ, states, (self.q0, other.q0), delta, accepts)

	# def union(self, other):
	# 	return self.cross(other, bool.__or__, f'{self.name}_or_{other.name}')

	# def intersect(self, other):
	# 	return self.cross(other, bool.__and__, f'{self.name}_and_{other.name}')

	# def is_subset_of(self, other):
	# 	'''
	# 		let A, B both be DFAs
	# 		C := B intersect A^c
	# 		A is a subset of B iff C does not have any acceptable strings
	# 	'''
	# 	# self (A) is subset of self (B)
	# 	# new = self.intersect(~other)
	# 	# if new.get_accepted():
	# 	# 	return False
	# 	# return True
	# 	return not self.intersect(~other).get_accepted()

	# def __contains__(self, other):
	# 	# other (A) in self (B)
	# 	new = other.intersect(~self)
	# 	if new.get_accepted():
	# 		return False
	# 	return True
	# 	# return self.subset(other)

	# def __eq__(self, other):
	# 	'''
	# 		Note: this was already here before commiting Task Complete #20
	# 		if both sides are a subset of each other then they are equal
	# 	'''
	# 	return self in other and other in self

	# def __invert__(self):
	# 	'''
	# 		returns the complement of the DFA with a new name
	# 	'''
	# 	return DFA(f'{self.name}_c', self.Σ, self.Q, self.q0, self.δ, self.Q - self.F)