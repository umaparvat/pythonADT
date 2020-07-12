import os
import sys
sys.path.append(os.getcwd())
from arrays.array import Array

def main():
	newArray = Array(5)
	print(len(newArray))
	newArray[4] = "hello"
	print(newArray[4])
	for i in range(5):
		newArray[i] = i
	for i in range(5):
		print(newArray[i])


if __name__ == "__main__":
	main()
