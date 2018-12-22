import re
from datetime import datetime
from log_entry import LogEntry


_YEAR = "year"
_MONTH = "month"
_DAY = "day"
_HOUR = "hour"
_MINUTE = "minute"
_GUARD_ID = "guard_id"
_EVENT = "event"


class LogParser:

    def __init__(self):
        self._guard_regex = re.compile("\[(?P<year>[0-9]+)-(?P<month>[0-9]+)-(?P<day>[0-9]+) "
                                       "(?P<hour>[0-9]+):(?P<minute>[0-9]+)\] "
                                       "Guard #(?P<guard_id>[0-9]+) "
                                       "(?P<event>[a-z ]+)")

        self._other_events_regex = re.compile("\[(?P<year>[0-9]+)-(?P<month>[0-9]+)-(?P<day>[0-9]+) "
                                              "(?P<hour>[0-9]+):(?P<minute>[0-9]+)\] "
                                              "(?P<event>[a-z ]+)")

    def parse(self, log_input):
        log_entry = None

        if log_input is not None:
            if self.is_start_of_shift_log_entry(log_input):
                matches = self._guard_regex.match(log_input)

                if matches:
                    log_entry = self.create_start_of_shift_log_entry(matches)
            else:
                matches = self._other_events_regex.match(log_input)

            if matches:
                log_entry = self.create_log_entry(matches)

        return log_entry

    @staticmethod
    def is_start_of_shift_log_entry(log_input):
        return log_input.find("Guard") > 0

    @staticmethod
    def create_start_of_shift_log_entry(matches):
        log_entry = LogEntry()
        log_entry.event_datetime = datetime(int(matches[_YEAR]), int(matches[_MONTH]), int(matches[_DAY]),
                                            int(matches[_HOUR]), int(matches[_MINUTE]))
        log_entry.guard_id = int(matches[_GUARD_ID])
        log_entry.event = matches[_EVENT]

        return log_entry

    @staticmethod
    def create_log_entry(matches):
        log_entry = LogEntry()
        log_entry.event_datetime = datetime(int(matches[_YEAR]), int(matches[_MONTH]), int(matches[_DAY]),
                                            int(matches[_HOUR]), int(matches[_MINUTE]))
        log_entry.event = matches[_EVENT]

        return log_entry
