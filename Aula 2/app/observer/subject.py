from .observer import Observer

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state: str):
        self._state = state
        self.notify_observers()