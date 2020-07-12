import sys
import os
sys.path.append(os.getcwd())
from adt.myfraction import MyFraction


def main():
    myfra = MyFraction("2/3")
    print(myfra)
    myfr1 = MyFraction("3/2")
    print(myfra, "*", myfr1, end="=")
    res = myfr1 * myfra
    print(res)
    myfr2 = MyFraction("-4/5")
    print(myfra, "/", myfr2, end="=")
    re2 = myfra/myfr2
    print(re2)
    print(myfra,"+", myfr1, end="=")
    print((myfra+myfr1))
    print(myfra, "-", myfr1, end="=")
    print((myfra-myfr1))
    ft = MyFraction(12.24)
    print(ft)


if __name__ == '__main__':
    main()

