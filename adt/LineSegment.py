from adt.point import point

class LineSegment:

	def __init__(self, ptA, ptB):
		self.ptA = ptA
		self.ptB = ptB

	def endPointA(self):
		return self.ptA.getX(), self.ptA.getY()

	def endPointB(self):
		return self.ptB.getX(), self.ptB.getY()

	def length():
		return self.ptB.distance(self.ptA)

	def toString():
		return f" ({self.ptA.getX()}, {self.ptA.getY()})#({self.ptB.getX(), self.ptB.getY()})"

	def isVertical(self):
		return self.ptA.getX() == self.ptB.getX()

	def isHorizontal(self):
		return self.ptA.getY() == self.ptB.getY()

	def isParallel(self, otherLine):
		return self.ptA.getX() == otherLine.ptA.getX() and self.ptB.getX() == otherLine.ptB.getX()

	def slope(self):
		if self.isVertical():
			return None
		run = self.ptA.getX() - self.ptB.getX()
		rise = self.pta.getY() - self.ptB.getY()
		return rise/run

	def isPerpendicular(self, otherLine):
		"""
		  slope1 = - 1/ otherslope is perpendicular
		"""
		own_slope = self.slope()
		other_slope = otherLine.slope()
		if own_slope is None or otherslope is None:
			return None
		return own_slope == (-1/otherslope)

	def shift(self, xInc, yInc):
		self.ptA.shift(xInc, yInc)
		self.ptB.shift(xInc, yInc)

	def midPoint(self):
		mid_x = self.ptA.getx() + self.ptB.getX() / 2
		mid_y = self.ptA.getX() + self.ptB.getY() / 2
		return mid_x, mid_y

	def intersects(self, otherLine):
		pass

	def bisects(self, otherLine):
		pass
	

