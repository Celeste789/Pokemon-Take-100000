from HistoryEvent import HistoryEvent


class History:
    def __init__(self):
        self.history = []

    def add(self, event: HistoryEvent):
        self.history.insert(0, event)

    def history_getter(self):
        return self.history
