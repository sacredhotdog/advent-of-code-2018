import unittest
from duplicate_frequency_detector import DuplicateFrequencyDetector


class TestDuplicateFrequencyDetector(unittest.TestCase):

    def test_duplicate_information_defaults_to_not_found(self):
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        self.assertIsNone(duplicate_frequency_detector.get_duplicate())
        self.assertEqual(duplicate_frequency_detector.duplicate_found(), False)

    def test_frequency_is_recorded_correctly_the_first_time(self):
        frequency_change = 77
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        duplicate_frequency_detector.record(frequency_change)

        self.assertEqual(duplicate_frequency_detector._frequencies.get(frequency_change), 1)

    def test_duplicated_frequency_is_recorded_correctly(self):
        frequency_change = 88
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        duplicate_frequency_detector.record(frequency_change)
        duplicate_frequency_detector.record(frequency_change)

        self.assertEqual(duplicate_frequency_detector._frequencies.get(frequency_change), 2)

    def test_no_more_recording_takes_place_after_a_duplicate_has_been_found(self):
        frequency_change_1 = 88
        frequency_change_2 = 99
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        duplicate_frequency_detector.record(frequency_change_1)
        duplicate_frequency_detector.record(frequency_change_2)
        duplicate_frequency_detector.record(frequency_change_1)
        duplicate_frequency_detector.record(frequency_change_2)

        self.assertEqual(duplicate_frequency_detector._frequencies.get(frequency_change_1), 2)
        self.assertEqual(duplicate_frequency_detector._frequencies.get(frequency_change_2), 1)

    def test_input_processed_correctly(self):
        frequency_changes = "+1\n-2\n+2\n"
        expected_result = 1
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        duplicate_frequency_detector.find_duplicates(frequency_changes)

        self.assertEqual(duplicate_frequency_detector.duplicate_found(), True)
        self.assertEqual(duplicate_frequency_detector.get_duplicate(), expected_result)

    def test_input_processed_correctly(self):
        # 1 -2 0 1
        frequency_changes = "+1\n-3\n+2"
        expected_result = 1
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        duplicate_frequency_detector.find_duplicates(frequency_changes)

        self.assertEqual(duplicate_frequency_detector.duplicate_found(), True)
        self.assertEqual(duplicate_frequency_detector.get_duplicate(), expected_result)

    def test_empty_line_input_processed_correctly(self):
        # 1 -2 0 1
        frequency_changes = "+1\n-3\n+2\n"
        expected_result = 1
        duplicate_frequency_detector = DuplicateFrequencyDetector()

        duplicate_frequency_detector.find_duplicates(frequency_changes)

        self.assertEqual(duplicate_frequency_detector.duplicate_found(), True)
        self.assertEqual(duplicate_frequency_detector.get_duplicate(), expected_result)


if __name__ == "__main__":
    unittest.main()
