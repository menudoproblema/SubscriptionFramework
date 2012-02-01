from subscription.signals.base import AbstractSignal
from subscription.signals.accumulators import AbstractAccumulator, NoneAccumulator


class Signal(AbstractSignal):
    def __init__(self, accumulator=None):
        if accumulator and not isinstance(accumulator, AbstractAccumulator):
            raise TypeError('accumulator must be an instance of AbstractAccumulator')

        self._accumulator = accumulator or NoneAccumulator()
        super(Signal, self).__init__()

    def get_accumulator(self):
        return self._accumulator
