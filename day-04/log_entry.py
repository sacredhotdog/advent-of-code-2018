BEGINS_SHIFT = "begins shift"
FALLS_ASLEEP = "falls asleep"
WAKES_UP = "wakes up"


class LogEntry:

    def __init__(self, entry_datetime=None, entry_guard_id=0, entry_event=None):
        self.event_datetime = entry_datetime
        self.guard_id = entry_guard_id
        self.event = entry_event

    @property
    def event_datetime(self):
        return self._event_date

    @event_datetime.setter
    def event_datetime(self, value):
        self._event_date = value

    @event_datetime.deleter
    def event_datetime(self):
        del self._event_date

    @property
    def guard_id(self):
        return self._guard_id

    @guard_id.setter
    def guard_id(self, value):
        self._guard_id = value

    @guard_id.deleter
    def guard_id(self):
        del self._guard_id

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    @event.deleter
    def event(self):
        del self._event

    def is_start_shift_event(self):
        return self._event == BEGINS_SHIFT

    def is_falls_asleep_event(self):
        return self._event == FALLS_ASLEEP

    def is_wakes_up_event(self):
        return self._event == WAKES_UP
