from claim_parser import ClaimParser


class Fabric:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = [[0 for y in range(width)] for x in range(height)]

    def get(self, x, y):
        return self._area[x][y]

    def place_claim(self, new_claim):
        if new_claim is not None:
            for x in range(new_claim.inches_from_top_edge, new_claim.inches_from_top_edge + new_claim.height):
                for y in range(new_claim.inches_from_left_edge, new_claim.inches_from_left_edge + new_claim.width):
                    content = self._area[x][y]

                    if not isinstance(content, str):
                        if content > 0:
                            self._area[x][y] = "X"
                        else:
                            self._area[x][y] = new_claim.claim_id

    def __str__(self):
        result = ""

        for x in range(self._height):
            for y in range(self._width):
                result += str(self._area[x][y]) + " "

            result += "\n"

        return result


def print_fabric():
    for i in range(1000):
        print_output = ""

        for j in range(1000):
            content = str(fabric.get(i, j))
            print_output += content + " " + (" " * (4 - len(content)))

        # !! 496 && 475 && 227
        print(print_output)


if __name__ == "__main__":
    with open("claims.txt") as file_object:
        file_content = file_object.read()

    fabric_width = 1000
    fabric_height = 1000
    fabric = Fabric(fabric_width, fabric_height)
    claim_parser = ClaimParser()

    for line in file_content.split("\n"):
        claim = claim_parser.parse(line)
        fabric.place_claim(claim)

    overlap_count = 0

    for row in range(fabric_height):
        for column in range(fabric_width):
            if fabric.get(row, column) == "X":
                overlap_count += 1

    print("Overlap count: " + str(overlap_count))
    # print_fabric()
