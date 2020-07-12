from ctypes import py_object

class Array:

	def __init__(self, size):
		assert size > 0, "size cannot be zero or less than zero"
		pyArray = py_object * size
		self._slot = pyArray()
		self._size = size
		self.clear(None)

	def __len__(self):
		return self._size

	def clear(self, value):
		for each in range(0, len(self)):
			self._slot[each] = value

	def __getitem__(self, index):
		assert 0 <= index < self._size, "Array subscript out of range"
		return self._slot[index]

	def __setitem__(self, index, value):
		assert 0 <= index < self._size, "Array subscript out of range"
		self._slot[index] = value


	def __iter__(self):
		return _ArrayIterator(self._slot)

class _ArrayIterator:
	def __init__(self, theArrayRef):
		self._theArray = theArrayRef
		self.currentInd = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.currentInd < len(self._theArray):
			result = self._theArray[self.currentInd]
			self.currentInd +=1
			return result
		else:
			raise StopIteration



