import unittest
from checksum import Checksum


class TestChecksum(unittest.TestCase):

    def test_correctly_detects_duplicated_letters(self):
        box_id = ["abbcde"]
        checksum = Checksum()

        checksum.process(box_id)

        self.assertEqual(len(checksum._results), 1)
        result = checksum._results[0]
        self.assertTrue(result.contains_duplicate)
        self.assertFalse(result.contains_triplicate)

    def test_correctly_detects_triplicated_letters(self):
        box_id = ["abcccde"]
        checksum = Checksum()

        checksum.process(box_id)

        self.assertEqual(len(checksum._results), 1)
        result = checksum._results[0]
        self.assertFalse(result.contains_duplicate)
        self.assertTrue(result.contains_triplicate)

    def test_correctly_detects_duplicated_and_triplicated_letters(self):
        box_id = ["aabcddde"]
        checksum = Checksum()

        checksum.process(box_id)

        self.assertEqual(len(checksum._results), 1)
        result = checksum._results[0]
        self.assertTrue(result.contains_duplicate)
        self.assertTrue(result.contains_triplicate)

    def test_correct_results_recorded_for_multiple_box_ids(self):
        box_ids = ["aabbccddeee", "abcde", "abcccde"]
        checksum = Checksum()

        checksum.process(box_ids)

        self.assertEqual(len(checksum._results), 3)
        result = checksum._results[0]
        self.assertTrue(result.contains_duplicate)
        self.assertTrue(result.contains_triplicate)
        result = checksum._results[1]
        self.assertFalse(result.contains_duplicate)
        self.assertFalse(result.contains_triplicate)
        result = checksum._results[2]
        self.assertFalse(result.contains_duplicate)
        self.assertTrue(result.contains_triplicate)

    def test_checksum_defaults_to_zero(self):
        checksum = Checksum()
        expected_result = 0

        self.assertEqual(checksum.calculate(), expected_result)

    def test_checksum_is_calculated_correctly_for_duplicated_letter_instance_only(self):
        box_id = "ee"
        expected_result = 0
        checksum = Checksum()

        checksum.process(box_id)

        self.assertEqual(checksum.calculate(), expected_result)

    def test_checksum_is_calculated_correctly_for_triplicated_letter_instance_only(self):
        box_id = "fff"
        expected_result = 0
        checksum = Checksum()

        checksum.process(box_id)

        self.assertEqual(checksum.calculate(), expected_result)

    def test_checksum_is_calculated_correctly_for_duplicated_and_triplicated_letter_instances(self):
        box_ids = ["aabbccddeee", "abcde", "abcccdde"]
        expected_result = 4
        checksum = Checksum()

        checksum.process(box_ids)

        self.assertEqual(checksum.calculate(), expected_result)


if __name__ == "__main__":
    unittest.main()
