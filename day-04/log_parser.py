import re
from datetime import date, time
from log_entry import LogEntry


class LogParser:

    def __init__(self):
        self._guard_regex = re.compile("\[([0-9]+)-([0-9]+)-([0-9]+) "
                                       "([0-9]+):([0-9]+)\] "
                                       "Guard #([0-9]+) ([a-z ]+)")
        self._other_events_regex = re.compile("\[([0-9]+)-([0-9]+)-([0-9]+) "
                                              "([0-9]+):([0-9]+)\] "
                                              "([a-z ]+)")

    def parse(self, log_input):
        if log_input is not None:
            if log_input.find("Guard") > 0:
                match = self._guard_regex.match(log_input)

                if match:
                    log_entry = LogEntry()
                    log_entry.event_date = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
                    log_entry.event_time = time(int(match.group(4)), int(match.group(5)))
                    log_entry.guard_id = int(match.group(6))
                    log_entry.event = match.group(7)

                    return log_entry
            else:
                match = self._other_events_regex.match(log_input)

            if match:
                log_entry = LogEntry()
                log_entry.event_date = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
                log_entry.event_time = time(int(match.group(4)), int(match.group(5)))
                log_entry.event = match.group(6)

                return log_entry

        return None
