import unittest
from log_entry import LogEntry
from datetime import datetime
from guard_activity import GuardActivity


class TestGuardActivity(unittest.TestCase):

    def test_sort_key_is_generated_correctly(self):
        log_entry = LogEntry(entry_datetime=datetime(1999, 1, 31, 15, 45))
        guard_activity = GuardActivity()
        expected_result = "199901311545"

        result = guard_activity.event_key(log_entry)

        self.assertEqual(result, expected_result)

    def test_log_items_are_sorted_correctly(self):
        log_entry1 = LogEntry(entry_datetime=datetime(2018, 11, 1, 1, 32), entry_event="falls asleep")
        log_entry2 = LogEntry(entry_datetime=datetime(2018, 12, 31, 23, 41), entry_event="wakes up")
        log_entry3 = LogEntry(datetime(2018, 10, 28, 0, 2), 700, "begins shift")
        guard_activity = GuardActivity()
        guard_activity.add_events([log_entry1, log_entry2, log_entry3])
        expected_result = [log_entry3, log_entry1, log_entry2]

        events = guard_activity.get_ordered_events()

        self.assertListEqual(events, expected_result)

    def test_nothing_should_be_processed_if_no_log_entries_are_present(self):
        guard_activity = GuardActivity()

        self.assertIsNone(guard_activity.get_ordered_events())

    def test_total_minutes_asleep_should_be_recorded_for_a_guard_correctly(self):
        guard_id = 700
        log_entry1 = LogEntry(datetime(2018, 1, 1, 0, 1), guard_id, "begins shift")
        log_entry2 = LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep")
        log_entry3 = LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 3), entry_event="wakes up")
        log_entry4 = LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 4), entry_event="falls asleep")
        log_entry5 = LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 5), entry_event="wakes up")
        guard_activity = GuardActivity()
        guard_activity.add_events([log_entry1, log_entry2, log_entry3, log_entry4, log_entry5])
        expected_result = 2

        result = guard_activity.get_total_time_asleep(guard_id)

        self.assertEqual(result, expected_result)

    def test_none_is_not_a_valid_entry(self):
        log_entry1 = LogEntry(datetime(2018, 1, 1, 0, 1), 700, "begins shift")
        log_entry2 = None
        guard_activity = GuardActivity()

        self.assertRaises(AttributeError, guard_activity.add_events, [log_entry1, log_entry2])

    def test_total_mismatched_log_entries_should_be_handled_correctly(self):
        guard_id = 701
        log_entry1 = LogEntry(datetime(2018, 1, 1, 0, 1), guard_id, "begins shift")
        log_entry2 = LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep")
        guard_activity = GuardActivity()
        guard_activity.add_events([log_entry1, log_entry2])
        expected_result = 0

        result = guard_activity.get_total_time_asleep(guard_id)

        self.assertEqual(result, expected_result)

    def test_total_sleepiest_guard_id_should_be_recorded_correctly(self):
        guard_activity = GuardActivity()
        guard_activity.add_events(
            [LogEntry(datetime(2018, 1, 1, 0, 1), 700, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 5), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 6), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 8), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 2, 0, 1), 701, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 4), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 5), entry_event="wakes up")])
        expected_result = 700

        result = guard_activity.get_sleepiest_guard()

        self.assertEqual(result, expected_result)

    def test_total_sleepiest_guard_time_asleep_should_be_recorded_correctly(self):
        guard_activity = GuardActivity()
        guard_activity.add_events(
            [LogEntry(datetime(2018, 1, 1, 0, 1), 700, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 5), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 6), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 8), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 2, 0, 1), 701, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 4), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 5), entry_event="wakes up")])
        expected_result = 5

        guard_id = guard_activity.get_sleepiest_guard()
        result = guard_activity.get_total_time_asleep(guard_id)

        self.assertEqual(result, expected_result)

    def test_correct_times_are_returned_for_a_guard(self):
        guard_id = 700
        guard_activity = GuardActivity()
        guard_activity.add_events(
            [LogEntry(datetime(2018, 1, 1, 0, 1), guard_id, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 5), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 6), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 8), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 2, 0, 1), 701, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 4), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 5), entry_event="wakes up")])
        expected_result = [[datetime(2018, 1, 1, 0, 2), datetime(2018, 1, 1, 0, 5)],
                           [datetime(2018, 1, 1, 0, 6), datetime(2018, 1, 1, 0, 8)]]

        result = guard_activity.get_times_for_guard(guard_id)

        self.assertListEqual(result, expected_result)

    def test_most_common_minute_asleep_is_correctly_reported(self):
        guard_id = 700
        guard_activity = GuardActivity()
        guard_activity.add_events(
            [LogEntry(datetime(2018, 1, 1, 0, 1), guard_id, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 5), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 6), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 8), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 2, 0, 1), guard_id, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 9), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 10), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 3, 0, 1), guard_id, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 11), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 12), entry_event="wakes up")])
        expected_most_common_minute = 2
        expected_count = 3

        minute_result, count_result = guard_activity.get_most_common_time_asleep(guard_id)

        self.assertEqual(minute_result, expected_most_common_minute)
        self.assertEqual(count_result, expected_count)

    def test_most_common_minute_asleep_is_correctly_reported_across_all_guards(self):
        expected_guard_id = 700
        guard_activity = GuardActivity()
        guard_activity.add_events(
            [LogEntry(datetime(2018, 1, 1, 0, 1), expected_guard_id, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 5), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 6), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 1, 0, 8), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 2, 0, 1), expected_guard_id, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 9), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 2, 0, 10), entry_event="wakes up"),
             LogEntry(datetime(2018, 1, 3, 0, 1), 701, "begins shift"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 2), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 3), entry_event="wakes up"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 11), entry_event="falls asleep"),
             LogEntry(entry_datetime=datetime(2018, 1, 3, 0, 12), entry_event="wakes up")])
        expected_most_common_minute = 2
        expected_count = 2

        guard_id_result, minute_result, count_result = guard_activity.get_most_common_time_asleep_for_all_guards()

        self.assertEqual(guard_id_result, expected_guard_id)
        self.assertEqual(minute_result, expected_most_common_minute)
        self.assertEqual(count_result, expected_count)


if __name__ == "__main__":
    unittest.main()
