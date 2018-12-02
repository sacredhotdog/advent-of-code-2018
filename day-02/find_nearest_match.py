from difflib import SequenceMatcher


class FindNearestMatch:

    def __init__(self):
        self._matcher = SequenceMatcher()
        self._results = {}

    def calculate_single_character_percentage(self, box_id):
        box_id_length = len(box_id)

        return 1 / box_id_length

    def find(self, box_ids):
        for this_box_id in box_ids:
            if this_box_id is None:
                continue

            if len(this_box_id) > 0:
                this_box_id = this_box_id.replace(" ", "")
                threshold = 1.0 - self.calculate_single_character_percentage(this_box_id)

                for that_box_id in box_ids:
                    if that_box_id is None:
                        continue

                    if this_box_id == that_box_id:
                        continue

                    self._matcher.set_seqs(this_box_id, that_box_id)
                    match_ratio = self._matcher.ratio()

                    if match_ratio == threshold:
                        if self._results.get(this_box_id) is not None:
                            self._results[this_box_id].append(that_box_id)
                        else:
                            self._results[this_box_id] = [that_box_id]

    def get_results(self):
        return self._results

    def get_matching_characters(self):
        # NB! Assumes only two possible matches

        key = list(self._results.keys())[0]
        first_match = self._results.get(key)[0]
        self._matcher.set_seqs(key, first_match)

        matching_blocks = self._matcher.get_matching_blocks()
        difference_index = matching_blocks[0].size
        matching_characters = first_match[0:difference_index]
        matching_characters += first_match[difference_index+1:]

        return matching_characters


if __name__ == "__main__":
    file_name = "box_ids.txt"

    with open(file_name) as file_object:
        file_content = file_object.read()

    find_nearest_match = FindNearestMatch()
    find_nearest_match.find(file_content.split("\n"))
    result = find_nearest_match.get_matching_characters()

    print(" -> " + result)
