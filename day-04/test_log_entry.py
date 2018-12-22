import unittest
from log_entry import LogEntry
from datetime import datetime


class TestLogEntry(unittest.TestCase):

    def test_default_values_are_correct(self):
        log_entry = LogEntry()

        self.assertIsNone(log_entry.event_datetime)
        self.assertEqual(log_entry.guard_id, 0)
        self.assertIsNone(log_entry.event)

    def test_initialisation_should_be_correct(self):
        expected_datetime = datetime(1999, 12, 31, 13, 14, 59)
        expected_guard_id = 1
        expected_event = "begins shift"

        log_entry = LogEntry(expected_datetime, expected_guard_id, expected_event)

        self.assertEqual(log_entry.event_datetime, expected_datetime)
        self.assertEqual(log_entry.guard_id, expected_guard_id)
        self.assertEqual(log_entry.event, expected_event)

    def test_is_shift_start_event_should_be_reported_correctly(self):
        expected_datetime = datetime(1999, 12, 31, 13, 14, 59)
        expected_guard_id = 1
        expected_event = "begins shift"

        log_entry = LogEntry(expected_datetime, expected_guard_id, expected_event)

        self.assertTrue(log_entry.is_start_shift_event())

    def test_is_falls_asleep_event_should_be_reported_correctly(self):
        expected_datetime = datetime(1999, 12, 31, 13, 14, 59)
        expected_event = "falls asleep"

        log_entry = LogEntry(entry_datetime=expected_datetime, entry_event=expected_event)

        self.assertTrue(log_entry.is_falls_asleep_event())

    def test_is_wakes_up_event_should_be_reported_correctly(self):
        expected_datetime = datetime(1999, 12, 31, 13, 14, 59)
        expected_event = "wakes up"

        log_entry = LogEntry(entry_datetime=expected_datetime, entry_event=expected_event)

        self.assertTrue(log_entry.is_wakes_up_event())


if __name__ == "__main__":
    unittest.main()
