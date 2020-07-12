import os
import sys
sys.path.append(os.getcwd())
from arrays.mylist import MyList

def main():
	lst = MyList()
	print(len(lst))
	lst.append("hello")
	lst.append("hi")
	lst.append(1)
	lst.append(3)
	print(lst)
	print(len(lst))
	lst.pop(1)
	print(lst)
	print(len(lst))
	print(lst.index(3))
	lst[0]="me"
	print(lst)
	lst.insert(1, "ppp")
	print(lst)
	lst.insert(3, "df")
	print(lst)
	lst.insert(0, "first")
	print(lst)
	print(lst.pop())
	print(lst)
	print(lst.pop())
	print(lst)
	print(lst.index("first"), lst.index("ppp"))
	print(lst.remove("first"))
	print(lst)
	print(lst.pop())
	print(lst.pop())
	print(lst.pop())
	print(lst)
if __name__ == "__main__":
	main()