class Complex:
	def __init__(self, r, i):
		self.r=r
		self.i=i
	def mod(self):
		modc=((((self.r)**2 + (self.i)**2)**0.5))
		return print('{:.2f}+0.00i'.format(modc.real))
#--------------------------------
	def __add__(self,D):
		sum=complex(self.r, self.i)+complex(D)
		if sum.imag>=0:
			return ('{:.2f}+{:.2f}i'.format(sum.real,sum.imag))
		else:
			return ('{:.2f}{:.2f}i'.format(sum.real,sum.imag))
#--------------------------------
	def __sub__(self,D):
		sub=complex(self.r, self.i)-complex(D)
		if sub.imag>=0:
			return ('{:.2f}+{:.2f}i'.format(sub.real,sub.imag))
		else:
			return ('{:.2f}{:.2f}i'.format(sub.real,sub.imag))
#---------------------------
	def __mul__(self,D):
		mul=(complex(self.r, self.i)*complex(D))
		if mul.imag>=0:
			return ('{:.2f}+{:.2f}i'.format(mul.real,mul.imag))
		else:
			return ('{:.2f}{:.2f}i'.format(mul.real,mul.imag))
#----------------------------
	def __truediv__(self,D):
		try:
			div=(complex(self.r, self.i)/complex(D))
			if div.imag>=0:
				return ('{:.2f}+{:.2f}i'.format(div.real,abs(div.imag)))
			else:
				return ('{:.2f}{:.2f}i'.format(div.real,div.imag))
		except: return 
#----------------------------
	def mod(self):
		modc=((((self.r)**2 + (self.i)**2)**0.5))
		return ('{:.2f}+0.00i'.format(modc))
#----------------------------
	def __complex__(self):
		return complex(self.r, self.i)
