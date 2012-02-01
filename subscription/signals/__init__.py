from subscription.signals.base import AbstractSignal
from subscription.signals.accumulators import NoneAccumulator


class Signal(AbstractSignal):
    def __init__(self, accumulator=None):
        self._accumulator = accumulator or NoneAccumulator()

    def get_accumulator(self):
        self._accumulator
