from log_parser import LogParser
import statistics


TIME_ASLEEP_KEY = "time_asleep"
GUARD_ID_KEY = "guard_id"
TIMES_KEY = "times"
MINUTES_ASLEEP_KEY = "minutes_asleep"


class GuardActivity:

    def __init__(self):
        self._log_entries = None
        self._guard_data = {}
        self._sleepist_guard = {GUARD_ID_KEY: 0, TIME_ASLEEP_KEY: 0}

    def event_key(self, event):
        datetime_key = event.event_datetime.strftime("%Y%m%d%H%M")

        return datetime_key

    def add_events(self, log_entries):
        self._log_entries = sorted(log_entries, key=self.event_key)

        self.process_events()

    def process_events(self):
        if self._log_entries is not None:
            guard_id = 0
            falls_asleep_time = None
            wakes_up_time = None

            for log_entry in self._log_entries:
                if log_entry.is_start_shift_event():
                    guard_id = log_entry.guard_id

                    if self._guard_data.get(guard_id) is None:
                        self._guard_data[guard_id] = {MINUTES_ASLEEP_KEY: 0, TIMES_KEY: []}
                elif log_entry.is_falls_asleep_event():
                    falls_asleep_time = log_entry.event_datetime
                elif log_entry.is_wakes_up_event():
                    wakes_up_time = log_entry.event_datetime
                    minutes_aleep = int((wakes_up_time - falls_asleep_time).total_seconds()) / 60

                    self._guard_data[guard_id][MINUTES_ASLEEP_KEY] += minutes_aleep
                    self._guard_data[guard_id][TIMES_KEY].append([falls_asleep_time, wakes_up_time])

                    if self._guard_data[guard_id][MINUTES_ASLEEP_KEY] > self._sleepist_guard[TIME_ASLEEP_KEY]:
                        self._sleepist_guard[GUARD_ID_KEY] = guard_id
                        self._sleepist_guard[TIME_ASLEEP_KEY] = self._guard_data[guard_id][MINUTES_ASLEEP_KEY]

                    falls_asleep_time = None
                    wakes_up_time = None

    def get_total_time_asleep(self, guard_id):
        if self._guard_data.get(guard_id) is not None:
            return self._guard_data[guard_id][MINUTES_ASLEEP_KEY]

    def get_ordered_events(self):
        return self._log_entries

    def get_sleepiest_guard(self):
        return self._sleepist_guard[GUARD_ID_KEY]

    def get_times_for_guard(self, guard_id):
        return self._guard_data[guard_id][TIMES_KEY]

    def get_most_common_time_asleep(self, guard_id):
        times = self.get_times_for_guard(guard_id)
        data = []

        for time_entry in times:
            start_minutes = time_entry[0].minute
            end_minutes = time_entry[1].minute

            for minute in range(start_minutes, end_minutes):
                data.append(minute)

        return statistics.mode(data)


if __name__ == "__main__":
    log_entries = []

    with open("guard-log.txt") as file_object:
        file_content = file_object.read()
        log_parser = LogParser()

        for line in file_content.split("\n"):
            if line:
                log_entries.append(log_parser.parse(line))

    guard_activity = GuardActivity()
    guard_activity.add_events(log_entries)
    sleepiest_guard_id = guard_activity.get_sleepiest_guard()

    time_asleep = guard_activity.get_total_time_asleep(sleepiest_guard_id)
    print(" -> Sleepiest guard: " + str(sleepiest_guard_id) + " (slept for " + str(time_asleep) + " minutes)")

    most_common_minute_asleep = guard_activity.get_most_common_time_asleep(sleepiest_guard_id)
    print(" -> Most common minute asleep: " + str(most_common_minute_asleep))

    print(" -> ID x most common minute: " + str(sleepiest_guard_id * most_common_minute_asleep))
