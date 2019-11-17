from char import Char

class regex():
	def __repr__(self):
		return ""

class re_null(regex):
	def __init__(self):
		pass

class re_eps(regex):
	def __init__(self):
		pass

class re_c(regex):
	def __init__(self, c):
		if isinstance(c, str):
			c = Char(c)
		self.c = c

class re_u(regex):
	def __init__(self, lc, rc):
		self.l = lc
		self.r = rc

class re_cat(regex):
	def __init__(self, lc, rc):
		self.l = lc
		self.r = rc

class re_star(regex):
	def __init__(self, r):
		self.r = r