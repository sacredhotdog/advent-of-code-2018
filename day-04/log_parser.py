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
        if log_input is not None:
            if log_input.find("Guard") > 0:
                matches = self._guard_regex.match(log_input)

                if matches:
                    log_entry = LogEntry()
                    log_entry.event_datetime = datetime(int(matches[_YEAR]), int(matches[_MONTH]), int(matches[_DAY]),
                                                        int(matches[_HOUR]), int(matches[_MINUTE]))
                    log_entry.guard_id = int(matches[_GUARD_ID])
                    log_entry.event = matches[_EVENT]

                    return log_entry
            else:
                matches = self._other_events_regex.match(log_input)

            if matches:
                log_entry = LogEntry()
                log_entry.event_datetime = datetime(int(matches[_YEAR]), int(matches[_MONTH]), int(matches[_DAY]),
                                                    int(matches[_HOUR]), int(matches[_MINUTE]))
                log_entry.event = matches[_EVENT]

                return log_entry

        return None
