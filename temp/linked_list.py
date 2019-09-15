class LinkedList:

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __len__(self):
        return 0

    def __add__(self, other):
        if self._first is None:
            self._first = other
