"""libraries for a set of timers.
"""

import time

__author__ = "Jonathan Fromentin"
__credits__ = ["Jonathan Fromentin"]
__license__ = "CeCILL version 2.1"
__version__ = "0.2.0"
__maintainer__ = "Jonathan Fromentin"


class OneShotTimer:
    """A simple one shot timer without interrupt that returns True when
    activated. It can be started or restarted avec the start method."""

    def __init__(self, period, start=True):
        self.period = period
        if start:
            self.start()
        else:
            self.is_started = False

    def start(self, period=None):
        """Start/restart the timer and set the period if specified. this method
        is useful if you want to start the timer after its instantiation or if
        you want to reuse the timer without having to recreate a new
        instance."""
        if period:
            self.period = period
        self.beginning = time.ticks_ms()
        self.is_started = True

    @property
    def is_activated(self):
        """Get the calculated value of is_activated."""
        if self.is_started:
            delta = time.ticks_diff(time.ticks_ms(), self.beginning)
            if delta > self.period:
                self.is_started = False
                return True
        return False


class PeriodicTimer:
    """A simple piriodic timer without interrupt that returns true when
    activated."""

    def __init__(self, period):
        self.period = period
        self.beginning = time.ticks_ms()

    @property
    def is_activated(self):
        """Get the calculated value of is_activated."""
        delta = time.ticks_diff(time.ticks_ms(), self.beginning)
        if delta > self.period:
            self.beginning = time.ticks_ms()
            return True
        return False
