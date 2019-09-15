import numpy as np


class Grid:

    def __init__(self, coordinates):
        number_of_coordinates = len(coordinates)
        self._coordinates = np.array(coordinates)
        self.max_width = int(max(self._coordinates[:number_of_coordinates, :1])) + 1
        self.max_height = int(max(self._coordinates[:number_of_coordinates, 1:2])) + 1

        self._populate_grid()

    def _populate_grid(self):
        self._data = np.empty((self.max_width, self.max_height), "S3")
        lowercase_alphabet = list(map(chr, range(97, 123)))
        uppercase_alphabet = list(map(chr, range(65, 91)))

        alphabet_count = 1
        alphabet_index = 0

        for x, y in self._coordinates:
            self._data[x][y] = uppercase_alphabet[alphabet_index] * alphabet_count

            if alphabet_index + 1 >= len(uppercase_alphabet):
                alphabet_count += 1
                alphabet_index = 0
            else:
                alphabet_index += 1

    def get(self, x, y):
        return self._data[x][y].decode("utf-8")

    @property
    def max_width(self):
        return self._max_width

    @max_width.setter
    def max_width(self, value):
        self._max_width = value

    @property
    def max_height(self):
        return self._max_height

    @max_height.setter
    def max_height(self, value):
        self._max_height = value
