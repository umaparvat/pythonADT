

class MyBag:
    def __init__(self):
        self._items = list()

    def __len__(self):
        """
        return the length of bag items
        O(1) both average and wrost case
        :return:
        """
        return len(self._items)

    def __contains(self, item):
        """
        returns item exists or not
        :param item:
        :return:
        Here it will be average O(n)
        """
        return item in self._items

    def add(self, item):
        """
        adds the item to the list
        complexity will be amortized O(1)
        :param item:
        :return:
        """
        self._items.append(item)

    def remove(self, item):
        ndx = self._items.index(item)
        self._items.pop(ndx)

    def __iter__(self):
        return _BagIterator(self._items)


class _BagIterator:
    def __init__(self, items):
        self.current_ndx = 0
        self._theitems = items

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_ndx < len(self._theitems):
            val = self._theitems[self.current_ndx]
            self.current_ndx +=1
            return val
        else:
            raise StopIteration