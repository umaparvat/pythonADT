from random import randint
class GrabBag:
    def __init__(self):
        self._items = list()

    def add(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def grabItem(self):
        random_ndx = randint(0, len(self)-1)
        return self._items.pop(random_ndx)



def main():
    grab_bag = GrabBag()
    grab_bag.add(3)
    grab_bag.add(3)
    grab_bag.add(5)
    print(grab_bag.grabItem())

if __name__ == "__main__":
    main()

