from char import Char
from string import String

def regex_generate(r):
	return String(r.generate())

class regex():
	def __repr__(self):
		return ""

class re_null(regex):
	def __init__(self):
		pass

class re_eps(regex):
	def __init__(self):
		pass

	def __repr__(self):
		return 'ε'

class re_c(regex):
	def __init__(self, c):
		if isinstance(c, str):
			c = Char(c)
		self.c = c

	def generate(self):
		return self.c

	def __repr__(self):
		return self.c.__repr__()

class re_u(regex):
	def __init__(self, lc, rc):
		self.l = lc
		self.r = rc

	def generate(self):
		return self.l.generate()

	def __repr__(self):
		return f'{self.l}∪{self.r}'

class re_cat(regex):
	def __init__(self, lc, rc):
		self.l = lc
		self.r = rc

	def generate(self):
		return f'{self.l.generate()}{self.r.generate()}'

	def __repr__(self):
		return f'{self.l}◦{self.r}'

class re_star(regex):
	def __init__(self, r):
		self.r = r

	def generate(self):
		return f'{self.r.generate()}'

	def __repr__(self):
		return f'({self.r})*'