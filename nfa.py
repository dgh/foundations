from dfa import DFA

class NFA(DFA):
	def __init__(self, name, Σ, Q, q0, δ, F):
		super(NFA, self).__init__(name, Σ, Q, q0, δ, F)

	def accepts(self, s):
		def lambda_closure(qi):
			stack = []
			visited = set()
			stack.append(qi)

			while stack:
				state = stack.pop()
				if state not in visited:
					visited.add(state)
					if self.δ[state].get('ε'):
						stack.extend(self.δ[state]['ε'])

			return visited

		states = lambda_closure(self.q0)

		for c in s:
			next_states = set()
			for qi in states:
				if self.δ[qi].get(c):
					for next_state in self.δ[qi][c]:
						next_states.update(lambda_closure(next_state))

			states.update(next_states)


		print('Could be in:', states)
		print('Accepting:', self.F)

		return True if (states & self.F) else False