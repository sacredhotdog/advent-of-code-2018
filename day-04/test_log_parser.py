import unittest
from datetime import datetime
from log_parser import LogParser


class TestLogParser(unittest.TestCase):

    def test_empty_string_is_ignored(self):
        log_parser = LogParser()

        result = log_parser.parse("")

        self.assertIsNone(result)

    def test_none_is_ignored(self):
        log_parser = LogParser()

        result = log_parser.parse(None)

        self.assertIsNone(result)

    def test_whitespace_only_is_ignored(self):
        log_parser = LogParser()

        result = log_parser.parse(" ")

        self.assertIsNone(result)

    def test_valid_begin_shift_input_is_parsed_correctly(self):
        expected_datetime = datetime(1518, 3, 25, 0, 1)
        expected_guard_id = 743
        expected_event = "begins shift"
        log_parser = LogParser()

        log_entry = log_parser.parse("[1518-03-25 00:01] Guard #743 begins shift")

        self.assertEqual(log_entry.event_datetime, expected_datetime)
        self.assertEqual(log_entry.guard_id, expected_guard_id)
        self.assertEqual(log_entry.event, expected_event)

    def test_valid_falls_asleep_input_is_parsed_correctly(self):
        expected_datetime = datetime(1619, 4, 26, 1, 2)
        expected_guard_id = 0
        expected_event = "falls asleep"
        log_parser = LogParser()

        log_entry = log_parser.parse("[1619-04-26 01:02] falls asleep")

        self.assertEqual(log_entry.event_datetime, expected_datetime)
        self.assertEqual(log_entry.guard_id, expected_guard_id)
        self.assertEqual(log_entry.event, expected_event)

    def test_valid_wakes_up_input_is_parsed_correctly(self):
        expected_datetime = datetime(1518, 10, 11, 0, 27)
        expected_guard_id = 0
        expected_event = "wakes up"
        log_parser = LogParser()

        log_entry = log_parser.parse("[1518-10-11 00:27] wakes up")

        self.assertEqual(log_entry.event_datetime, expected_datetime)
        self.assertEqual(log_entry.guard_id, expected_guard_id)
        self.assertEqual(log_entry.event, expected_event)


if __name__ == "__main__":
    unittest.main()
