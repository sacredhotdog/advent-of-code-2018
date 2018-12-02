import unittest
from find_nearest_match import FindNearestMatch


class TestFindNearestMatch(unittest.TestCase):

    def test_percentage_weight_of_a_single_character_is_calculated_correctly(self):
        box_id = "0123456789"
        find_nearest_match = FindNearestMatch()

        result = find_nearest_match.calculate_single_character_percentage(box_id)

        self.assertEqual(result, 0.1)

    def test_single_closest_match_should_be_reported_correctly(self):
        box_ids = ["0123456789", "1123456789"]
        find_nearest_match = FindNearestMatch()

        find_nearest_match.find(box_ids)

        self.assertEqual(len(find_nearest_match.get_results()), 2)

    def test_no_match_should_be_reported_correctly(self):
        box_ids = ["0123456789", "0000000000"]
        find_nearest_match = FindNearestMatch()

        find_nearest_match.find(box_ids)

        self.assertEqual(len(find_nearest_match.get_results()), 0)

    def test_no_match_should_be_reported_against_an_empty_box_id(self):
        box_ids = ["0123456789", ""]
        find_nearest_match = FindNearestMatch()

        find_nearest_match.find(box_ids)

        self.assertEqual(len(find_nearest_match.get_results()), 0)

    def test_no_match_should_be_reported_against_a_none_box_id(self):
        box_ids = ["0123456789", None]
        find_nearest_match = FindNearestMatch()

        find_nearest_match.find(box_ids)

        self.assertEqual(len(find_nearest_match.get_results()), 0)

    def test_get_matching_characters_should_be_correct(self):
        box_ids = ["0123456789", "1123456789"]
        find_nearest_match = FindNearestMatch()
        find_nearest_match.find(box_ids)

        result = find_nearest_match.get_matching_characters()

        self.assertEqual(result, "123456789")


if __name__ == "__main__":
    unittest.main()
