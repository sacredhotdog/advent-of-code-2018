import unittest
from log_entry import LogEntry
from datetime import date, time


class TestLogEntry(unittest.TestCase):

    def test_default_values_are_correct(self):
        log_entry = LogEntry()

        self.assertIsNone(log_entry.event_date)
        self.assertIsNone(log_entry.event_time)
        self.assertEqual(log_entry.guard_id, 0)
        self.assertIsNone(log_entry.event)

    def test_initialisation_should_be_correct(self):
        expected_date = date(1999, 12, 31)
        expected_time = time(13, 14, 59)
        expected_guard_id = 1
        expected_event = "begins shift"

        log_entry = LogEntry(expected_date, expected_time, expected_guard_id, expected_event)

        self.assertEqual(log_entry.event_date, expected_date)
        self.assertEqual(log_entry.event_time, expected_time)
        self.assertEqual(log_entry.guard_id, expected_guard_id)
        self.assertEqual(log_entry.event, expected_event)


if __name__ == "__main__":
    unittest.main()
