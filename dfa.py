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