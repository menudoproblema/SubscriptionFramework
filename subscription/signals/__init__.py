from subscription.signals.base import AbstractSignal
from subscription.signals.accumulators import (AbstractAccumulator,
    DefaultAccumulator)


class Signal(AbstractSignal):
    def __init__(self, accumulator=None):
        if accumulator:
            if callable(accumulator):
                accumulator = accumulator()

            if not isinstance(accumulator, AbstractAccumulator):
                raise TypeError('accumulator must be an instance of \
                    AbstractAccumulator')

        self._accumulator = accumulator or DefaultAccumulator()
        super(Signal, self).__init__()

    def get_accumulator(self):
        return self._accumulator
