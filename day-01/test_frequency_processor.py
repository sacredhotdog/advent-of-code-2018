import unittest
from frequency_processor import FrequencyProcessor


class TestFrequencyProcessor(unittest.TestCase):

    def setUp(self):
        self.frequency_processor = FrequencyProcessor()

    def test_frequency_processer_defaults_to_zero(self):
        result = self.frequency_processor.get_result()

        self.assertEqual(result, 0)

    def test_no_processing_performed_if_frequency_change_is_none(self):
        frequency_change = None
        expected_result = 0

        self.frequency_processor.process(frequency_change)

        result = self.frequency_processor.get_result()
        self.assertEqual(result, expected_result)

    def test_processes_single_frequency_change_correctly(self):
        frequency_change = "+1"
        expected_result = 1

        self.frequency_processor.process(frequency_change)

        result = self.frequency_processor.get_result()
        self.assertEqual(result, expected_result)

    def test_processes_multiple_frequency_changes_correctly(self):
        frequency_change_1 = "+1"
        frequency_change_2 = "-2"
        frequency_change_3 = "+4"
        expected_result = 3

        self.frequency_processor.process(frequency_change_1)
        self.frequency_processor.process(frequency_change_2)
        self.frequency_processor.process(frequency_change_3)

        result = self.frequency_processor.get_result()
        self.assertEqual(result, expected_result)

    def test_input_whitespace_is_removed(self):
        frequency_change = " + 7 \n "
        expected_result = "+7"

        result = self.frequency_processor.prepare_input(frequency_change)

        self.assertEqual(result, expected_result)

    def test_input_new_lines_are_removed(self):
        frequency_change = "+1\n"
        expected_result = "+1"

        result = self.frequency_processor.prepare_input(frequency_change)

        self.assertEqual(result, expected_result)

    def test_input_empty_lines_are_ignored(self):
        frequency_change = ""
        expected_result = None

        result = self.frequency_processor.prepare_input(frequency_change)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
