

class MyFraction:
	def __init__(self, numerator, denominator=1):
		if isinstance(numerator, str):
			self.numerator, self.denominator = map(int, numerator.split("/"))
		elif isinstance(numerator, float):
			num_aftr_dot = len(str(numerator).split(".")[1])
			denom = 10 ** num_aftr_dot
			num = int(numerator * denom)
			self.numerator, self.denominator = MyFraction._simplify(num,denom)
		else:
			self.numerator = numerator
			self.denominator = denominator
		assert not self.denominator == 0, "Denominator should not be 0"
		self.sign = self._convert_sign()

	def _convert_sign(self):
		if self.numerator < 0 and self.denominator < 0:
			self.numerator = self.numerator * -1
			self.denominator *= -1
			return True
		elif self.denominator < 0 and not self.numerator < 0:
			self.denominator *= -1
			self.numerator *=-1
			return False
		elif self.numerator < 0 and not self.denominator < 0:
			return False
		else:
			return True

	@staticmethod
	def _gcd(a, b):
		"""
		ecludian algorithm for finding gcd
		a*b = lcm(a,b)* gcd(a,b)
		"""
		if a == 0:
			return b
		return MyFraction._gcd(b % a, a)

	@staticmethod
	def _simplify(a,b):
		gcd = MyFraction._gcd(a, b)
		a //= gcd
		b //= gcd
		return a, b

	def __add__(self, otherFraction):
		if self.denominator == otherFraction.denominator:
			numerator = self.numerator + otherFraction.numerator
			denominator = self.denominator
		else:
			numerator = self.numerator * otherFraction.denominator + otherFraction.denominator * self.denominator
			denominator = self.denominator * otherFraction.denominator
		numerator, denominator = self._simplify(numerator, denominator)
		return MyFraction(numerator, denominator)

	def __sub__(self, otherFraction):
		if self.denominator == otherFraction.denominator:
			numerator = self.numerator - otherFraction.numerator
			denominator = self.denominator
		else:
			numerator = (self.numerator * otherFraction.denominator) - (otherFraction.denominator * self.denominator)
			denominator = self.denominator * otherFraction.denominator
		numerator, denominator = self._simplify(numerator, denominator)
		return MyFraction(numerator, denominator)

	def __mul__(self, otherFraction):
		numerator = self.numerator * otherFraction.numerator
		denominator = self.denominator * otherFraction.denominator
		numerator, denominator = self._simplify(numerator, denominator)
		return MyFraction(numerator, denominator)

	def __truediv__(self, otherFraction):
		numerator = self.numerator * otherFraction.denominator
		denominator = self.denominator * otherFraction.numerator
		numerator, denominator = self._simplify(numerator, denominator)
		return MyFraction(numerator, denominator)

	def __str__(self):
		return f"{int(self.numerator)}/{int(self.denominator)}" if int(self.denominator) != 0 and int(self.denominator) != 1 else f"{self.numerator}"







