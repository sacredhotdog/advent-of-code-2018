class LogEntry:

    def __init__(self, entry_date=None, entry_time=None, entry_guard_id=0, entry_event=None):
        self.event_date = entry_date
        self.event_time = entry_time
        self.guard_id = entry_guard_id
        self.event = entry_event

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, value):
        self._event_date = value

    @event_date.deleter
    def event_date(self):
        del self._event_date

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value

    @event_time.deleter
    def event_time(self):
        del self._event_time

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
