from char import Char
from string import String

class DFA():
	def __init__(self, name, Σ, Q, q0, δ, F):
		self.name = name
		self.Q = Q
		self.Σ = Σ
		self.q0 = q0
		self.δ = δ
		self.F = F

	def accepts(self, s):
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
		for i in range(len(s)):
			if self.δ[qi].get('_default'):
				qi =  self.δ[qi].get(s[i], self.δ[qi]['_default'])
			else:
				qi =  self.δ[qi][s[i]]
		return qi in self.F

	def trace(self, s):
		states = []
		if self.accepts(s):
			qi = self.q0
			for i in range(len(s)):
				states.append(qi)
				qi =  self.δ[qi].get(s[i], self.δ[qi]['_default'])
			return states

		return False