import os
import sys
sys.path.append(os.getcwd())
from arrays.array import Array

class MyList:
	def __init__(self):
		self._size = 1
		self._currentSize = 0
		self._elements = Array(self._size)

	def __len__(self):
		return self._currentSize

	def __getitem__(self, index):
		assert 0<= index < self._currentSize, "List index out of range"
		return self._elements[index]

	def __setitem__(self, index, value):
		assert 0<= index < self._currentSize, "List index out of range"
		self._elements[index] = value
		self._currentSize +=1

	def append(self, value):
		if self._currentSize < self._size:
			self._elements[self._currentSize] = value
			self._currentSize +=1
		else:			
			self._elements = self._expandArray()
			self._elements[self._currentSize] = value
			self._currentSize +=1
			self._size *=2

	def pop(self, index=None):
		if index is None:
			res = self._elements[self._currentSize-2]
			self._elements[self._currentSize-2] = None
			self._currentSize -=1
			return res
		else:
			res = self._elements[index]
			for i in range(index, len(self)-1):
				self._elements[i] = self._elements[i+1]
			self._currentSize -=1
			return res


	def _expandArray(self):
		newArray = Array(self._size*2)
		for i in range(len(self)):
			newArray[i] = self._elements[i]
		return newArray

	def insert(self, index, value):
		if self._currentSize == self._size:
			self._elements = self._expandArray()
		if index > self._currentSize-1 :
			self._elements[self._currentSize-1] = value
			self._currentSize +=1
			return
		next_val = self._elements[index]
		self._elements[index] = value
		for i in range(index+1, len(self)):
			tmp = self._elements[i]
			self._elements[i] = next_val
			next_val = tmp
		self._currentSize +=1
		return

	def index(self, value):
		for i in range(len(self)):
			if self._elements[i] == value:
				return i
		return -1

	def remove(self, value):
		ind = self.index(value)
		if ind != -1:
			return self.pop(ind)
		else:
			raise ValueError("x is not list")

	def clear(self, value=None):
		for i in range(len(self)):
			self._elements[i] = value

	def __iter__(self):
		return _MyListIterator(self._elements)

	def __str__(self):
		string = "["
		if self._currentSize == 0:
			return string+"]"
		for i in range(len(self)-1):
			string+= str(self._elements[i])+","
		string = string.rstrip(",")
		return string+"]"


class _MyListIterator:
	def __init__(self, theElements):
		self._theElements = theElements
		self._currentInd = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._currentInd < len(self._theElements):
			res = self._theElements[self._currentInd]
			if res is None:
				res = self._theElements[self._currentInd+1]
				self._currentInd +=2
				return res
			self._currentInd +=1
			return res
		else:
			raise StopIteration




