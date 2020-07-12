# import sys
# sys.path.append("C:\\Users\\kauma\\Documents\\Learning\\ADT")
from adt.exception_handling import ADTValueError
class CountingBag:
    def __init__(self):
        self._items = list()
        self.counter = dict()

    def _counter_ops(self, item, ops):
        if self.counter.get(item) == 0:
            del self.counter[item]
            return
        if item in self.counter:
            if ops == 'incr':
                self.counter[item] +=1
            else:
                self.counter[item] -=1
        else:
            if ops == 'incr':
                self.counter[item] = 1
        return


    def add(self, item):
        self._counter_ops(item, "incr")
        self._items.append(item)

    def remove(self, item):
        self._counter_ops(item, "decr")
        try:
            ndx = self._items.index(item)
            self._items.pop(ndx)
        except ValueError:
            raise ADTValueError(f"{item} is not in the Bag")

    def numOf(self, item):
        return self.counter.get(item, 0)



def main():
    mycount_bag = CountingBag()
    mycount_bag.add(1)
    mycount_bag.add(2)
    mycount_bag.add(2)
    mycount_bag.add(2)
    print(mycount_bag.numOf(2))
    mycount_bag.remove(2)
    mycount_bag.remove(2)
    mycount_bag.remove(2)
    print(mycount_bag.numOf(2))
    #mycount_bag.remove(2)


if __name__ == "__main__":
    main()