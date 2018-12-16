from claim_parser import ClaimParser


class Fabric:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = [[0 for y in range(width)] for x in range(height)]
        self._disputed_claim_locations = {}
        self._undisputed_claims = {}

    def get(self, x, y):
        return self._area[x][y]

    def place_claim(self, new_claim):
        if new_claim is not None:
            overlap_flag = False
            old_claim_ids = []

            for x in range(new_claim.inches_from_top_edge, new_claim.inches_from_top_edge + new_claim.height):
                for y in range(new_claim.inches_from_left_edge, new_claim.inches_from_left_edge + new_claim.width):
                    content = self._area[x][y]
                    dispute_key = str(x) + "," + str(y)

                    if not isinstance(content, str):
                        if content > 0:
                            overlap_flag = True
                            # TODO duplication of IDs
                            old_claim_ids.append(content)

                            if self._disputed_claim_locations.get(dispute_key) is None:
                                self._disputed_claim_locations[dispute_key] = []

                            if content not in self._disputed_claim_locations[dispute_key]:
                                self._disputed_claim_locations[dispute_key].append(content)
                                self._disputed_claim_locations[dispute_key].append(new_claim.claim_id)

                            self._area[x][y] = "X"
                            # TODO overlap counting can happen here instead - should be a bit faster
                        else:
                            self._area[x][y] = new_claim.claim_id
                    else:
                        # TODO overlap counting can happen here instead - should be a bit faster
                        overlap_flag = True

                        for disputed_claim_id in self._disputed_claim_locations[dispute_key]:
                            old_claim_ids.append(disputed_claim_id)

            if overlap_flag is True:
                for old_claim_id in old_claim_ids:
                    if self._undisputed_claims.get(old_claim_id) is not None:
                        del self._undisputed_claims[old_claim_id]
            else:
                self._undisputed_claims[new_claim.claim_id] = new_claim

    def undisputed_claims(self):
        return list(self._undisputed_claims.keys())

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

        print(print_output)


if __name__ == "__main__":
    with open("claims.txt") as file_object:
        file_content = file_object.read()

    fabric_width = 1000
    fabric_height = 1000
    fabric = Fabric(fabric_width, fabric_height)
    claim_parser = ClaimParser()

    for line in file_content.split("\n"):
        current_claim = claim_parser.parse(line)
        fabric.place_claim(current_claim)

    overlap_count = 0

    for row in range(fabric_height):
        for column in range(fabric_width):
            if fabric.get(row, column) == "X":
                overlap_count += 1

    print("Overlap count: " + str(overlap_count))
    print("Undisputed claims: " + str(fabric.undisputed_claims()))
