class Fabric:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = [[0 for y in range(width)] for x in range(height)]

    def get(self, x, y):
        return self._area[x][y]

    def place_claim(self, claim):
        for x in range(claim.inches_from_top_edge, claim.inches_from_top_edge + claim.height):
            for y in range(claim.inches_from_left_edge, claim.inches_from_left_edge + claim.width):
                if self._area[x][y] > 0:
                    self._area[x][y] = "X"
                else:
                    self._area[x][y] = claim.claim_id

    def __str__(self):
        result = ""

        for x in range(self._height):
            for y in range(self._width):
                result += str(self._area[x][y]) + " "

            result += "\n"

        return result
