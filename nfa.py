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
			next_states = set()
			for qi in states:
				for next_state in self.δ[qi][c]:
					next_states.update(epsilon_closure(next_state))

			states = next_states

		return True if (states & self.F) else False