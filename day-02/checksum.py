from result import Result


class Checksum:

    def __init__(self):
        self._results = []

    def process(self, box_ids):
        for box_id in box_ids:
            result = Result()

            while len(box_id) > 0:
                current_character = box_id[0]
                count = box_id.count(current_character)

                if count == 2:
                    result.contains_duplicate = True
                elif count == 3:
                    result.contains_triplicate = True

                if result.contains_duplicate and result.contains_triplicate:
                    break

                box_id = box_id.replace(current_character, "")

            self._results.append(result)

    def calculate(self):
        duplicate_count = 0
        triplicate_count = 0

        for result in self._results:
            if result.contains_duplicate:
                duplicate_count += 1
            if result.contains_triplicate:
                triplicate_count += 1

        return duplicate_count * triplicate_count


if __name__ == "__main__":
    checksum = Checksum()
    file_name = "box_ids.txt"

    with open(file_name) as file_object:
        file_content = file_object.read()
        checksum.process(file_content.split("\n"))

    print(" -> Checksum: " + str(checksum.calculate()))
