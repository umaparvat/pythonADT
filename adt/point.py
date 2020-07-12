from math import sqrt

class Point:
	def __init__(self, x, y):
		self.xCord = x
		self.yCord = y

	def getX():
		return self.xCord

	def getY():
		return self.yCord

	def distance(self, otherPoint):
		xDiff = self.xCord - otherPoint.xCord
		yDiff = self.yCord - otherPoint.yCord
		return sqrt( xDiff ** 2 + yDiff ** 2)

	def shift(self, incX, incY):
		self.xCord += incX
		self.yCord += incY
