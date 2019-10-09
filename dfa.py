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
		'''
			Transitioning with '_default' is useful for a 'shadow realm' state
			where you go to if an input is incorrect and the DFA won't accept it.
		'''
		if self.Q: 
			if not s:
				return False
			elif s == [Char()]:
				return True
		else:
			if s.is_empty():
				return True
			return False

		qi = self.q0
		for c in s:
			qi = self.δ[qi][c]

		return qi in self.F

	def get_accepted(self):
		'''
			Does not work with DFAs that utilize the '_default' key
			I will probably remove that because it looks like it will cause
			more problems down the road.
		'''
		v = set()
		a = []

		def accept(qi):
			if qi in self.F:
				return True
			elif qi in v:
				return False
			v.add(qi)

			for c in self.Σ:
				if accept(self.δ[qi][c]):
					a.append(c)
					return True
			return False

		accept(self.q0)

		return String(a[::-1], self.Σ)
		

	def trace(self, s):
		states = []
		if self.accepts(s):
			qi = self.q0
			for c in s:
				states.append(qi)
				qi =  self.δ[qi][c]
			return states

		return False