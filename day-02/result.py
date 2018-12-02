class Result:

    def __init__(self):
        self.contains_duplicate = False
        self.contains_triplicate = False

    @property
    def contains_duplicate(self):
        return self._contains_duplicate

    @contains_duplicate.setter
    def contains_duplicate(self, value):
        self._contains_duplicate = value

    @contains_duplicate.deleter
    def contains_duplicate(self):
        del self._contains_duplicate

    @property
    def contains_triplicate(self):
        return self._contains_triplicate

    @contains_triplicate.setter
    def contains_triplicate(self, value):
        self._contains_triplicate = value

    @contains_triplicate.deleter
    def contains_triplicate(self):
        del self._contains_triplicate
