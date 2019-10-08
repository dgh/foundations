from char import Char

class DFA():
	def __init__(self, name, Q, Σ, q0, δ, F):
		self.name = name
		self.Q = Q
		self.Σ = Σ
		self.q0 = q0
		self.δ = δ
		self.F = F

	def accepts(self, s):
		qi = self.q0
		for i in range(len(s)):
			qi = self.δ(qi, s[i])

		return self.F(qi)

	def trace(self, s):
		states = []
		if self.accepts(s):
			qi = self.q0
			for i in range(len(s)):
				states.append(qi)
				qi = self.δ(qi, s[i])
			return states

		return False