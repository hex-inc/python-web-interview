import time


class BusyLoopDetector:
    """
    Detects busy loops by tracking the number of calls within a time window.
    If the number of calls exceeds the threshold within the window, it raises
    an error to prevent infinite loops from consuming resources.
    """

    def __init__(self, threshold: int = 1000, time_window: float = 1.0):
        self._counter = 0
        self._threshold = threshold
        self._time_window = time_window
        self._start_time = time.monotonic()

    def _reset_timer(self) -> None:
        self._start_time = time.monotonic()
        self._counter = 0

    def check(self) -> None:
        self._counter += 1
        current_time = time.monotonic()

        if current_time - self._start_time > self._time_window:
            self._reset_timer()
        elif self._counter > self._threshold:
            raise RuntimeError("Busy loop detected")
