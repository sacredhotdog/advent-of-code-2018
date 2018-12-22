from log_parser import LogParser
from scipy import stats


_TIME_ASLEEP_KEY = "time_asleep"
_GUARD_ID_KEY = "guard_id"
_TIMES_KEY = "times"
_MINUTES_ASLEEP_KEY = "minutes_asleep"
_MOST_COMMON_MINUTE_KEY = "most_common_minute"
_COUNT_KEY = "count"


class GuardActivity:

    def __init__(self):
        self._log_entries = None
        self._guard_data = {}
        self._sleepist_guard = {_GUARD_ID_KEY: 0, _TIME_ASLEEP_KEY: 0}

    def add_events(self, log_entries):
        self._log_entries = sorted(log_entries, key=self.event_key)
        self.process_events()

    @staticmethod
    def event_key(event):
        datetime_key = event.event_datetime.strftime("%Y%m%d%H%M")

        return datetime_key

    def process_events(self):
        if self._log_entries is not None:
            current_guard_id = 0
            fell_asleep_at = None

            for log_entry in self._log_entries:
                if log_entry.is_start_shift_event():
                    current_guard_id = log_entry.guard_id

                    if self._guard_data.get(current_guard_id) is None:
                        self._guard_data[current_guard_id] = {_MINUTES_ASLEEP_KEY: 0, _TIMES_KEY: []}
                elif log_entry.is_falls_asleep_event():
                    fell_asleep_at = log_entry.event_datetime
                elif log_entry.is_wakes_up_event():
                    woke_up_at = log_entry.event_datetime
                    minutes_aleep = self.convert_seconds_to_minutes(fell_asleep_at, woke_up_at)

                    self._guard_data[current_guard_id][_MINUTES_ASLEEP_KEY] += minutes_aleep
                    self._guard_data[current_guard_id][_TIMES_KEY].append([fell_asleep_at, woke_up_at])

                    if self._guard_data[current_guard_id][_MINUTES_ASLEEP_KEY] > self._sleepist_guard[_TIME_ASLEEP_KEY]:
                        self._sleepist_guard[_GUARD_ID_KEY] = current_guard_id
                        self._sleepist_guard[_TIME_ASLEEP_KEY] = self._guard_data[current_guard_id][_MINUTES_ASLEEP_KEY]

    @staticmethod
    def convert_seconds_to_minutes(fell_asleep_at, woke_up_at):
        return (woke_up_at - fell_asleep_at).total_seconds() / 60

    def get_total_time_asleep(self, guard_id):
        if self._guard_data.get(guard_id) is not None:
            return self._guard_data[guard_id][_MINUTES_ASLEEP_KEY]

    def get_ordered_events(self):
        return self._log_entries

    def get_sleepiest_guard(self):
        return self._sleepist_guard[_GUARD_ID_KEY]

    def get_times_for_guard(self, guard_id):
        return self._guard_data[guard_id][_TIMES_KEY]

    def get_most_common_time_asleep(self, guard_id):
        times = self.get_times_for_guard(guard_id)
        data = []

        for time_entry in times:
            start_minutes = time_entry[0].minute
            end_minutes = time_entry[1].minute

            for minute in range(start_minutes, end_minutes):
                data.append(minute)

        mode = stats.mode(data)

        return mode[0], mode[1]

    def get_most_common_time_asleep_for_all_guards(self):
        result = {_GUARD_ID_KEY: 0, _MOST_COMMON_MINUTE_KEY: 0, _COUNT_KEY: 0}

        for guard_key, guard_value in self._guard_data.items():
            most_common_minute, no_of_occurrences = self.get_most_common_time_asleep(guard_key)

            if no_of_occurrences > result[_COUNT_KEY]:
                result[_GUARD_ID_KEY] = guard_key
                result[_MOST_COMMON_MINUTE_KEY] = most_common_minute
                result[_COUNT_KEY] = no_of_occurrences

        return result[_GUARD_ID_KEY], result[_MOST_COMMON_MINUTE_KEY], result[_COUNT_KEY]


if __name__ == "__main__":
    all_log_entries = []

    with open("guard-log.txt") as file_object:
        file_content = file_object.read()
        log_parser = LogParser()

        for line in file_content.split("\n"):
            if line:
                all_log_entries.append(log_parser.parse(line))

    guard_activity = GuardActivity()
    guard_activity.add_events(all_log_entries)
    sleepiest_guard_id = guard_activity.get_sleepiest_guard()

    time_asleep = guard_activity.get_total_time_asleep(sleepiest_guard_id)
    print("Sleepiest guard: " + str(sleepiest_guard_id) + " (slept for " + str(time_asleep) + " minutes)")

    most_common_minute_asleep = guard_activity.get_most_common_time_asleep(sleepiest_guard_id)
    print("Most common minute asleep: " + str(most_common_minute_asleep))

    print(" -> Part 1 answer: guard ID x most common minute = " + str(sleepiest_guard_id * most_common_minute_asleep))

    sleepiest_guard_id, most_common_minute_asleep, count = guard_activity.get_most_common_time_asleep_for_all_guards()
    print("Guard " + str(sleepiest_guard_id) + " was asleep " + str(count) + " times at minute " + str(
        most_common_minute_asleep))

    print(" -> Part 2 answer: guard ID x most common minute = " + str(sleepiest_guard_id * most_common_minute_asleep))
