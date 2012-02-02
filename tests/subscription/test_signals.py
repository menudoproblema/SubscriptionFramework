import unittest
from subscription.signals import Signal
from subscription.signals.accumulators import *


def handler_none(*args, **kwargs):
    return None


def handler_true(*args, **kwargs):
    return True


def handler_false(*args, **kwargs):
    return False


def handler_zero(*args, **kwargs):
    return 0


def handler_one(*args, **kwargs):
    return 1


def handler_two(*args, **kwargs):
    return 2


class SignalTest(unittest.TestCase):
    def test_signal(self):
        signal = Signal()
        self.assertEqual(signal.has_handlers(), False)

        signal.connect(handler_none)
        self.assertEqual(signal.has_handlers(), True)
        self.assertEqual(signal.count_handlers(), 1)

        signal.connect(handler_true)
        self.assertEqual(signal.has_handlers(), True)
        self.assertEqual(signal.count_handlers(), 2)

        signal.connect(handler_false)
        self.assertEqual(signal.has_handlers(), True)
        self.assertEqual(signal.count_handlers(), 3)

        signal.disconnect(handler_false)
        self.assertEqual(signal.has_handlers(), True)
        self.assertEqual(signal.count_handlers(), 2)

        signal.clear()
        self.assertEqual(signal.has_handlers(), False)
        self.assertEqual(signal.count_handlers(), 0)

        del signal

    def test_get_accumulator(self):
        signal = Signal()
        is_instance = isinstance(signal.get_accumulator(), DefaultAccumulator)
        self.assertTrue(is_instance)
        del signal

        signal = Signal(accumulator=SumAccumulator)
        is_instance = isinstance(signal.get_accumulator(), SumAccumulator)
        self.assertTrue(is_instance)
        del signal

    def test_noneaccumulator(self):
        signal = Signal(accumulator=NoneAccumulator)
        signal.connect(handler_none)
        signal.connect(handler_true)
        signal.connect(handler_false)
        val = signal.emit()
        self.assertEqual(val, None)
        del signal

    def test_sumaccumulator(self):
        signal = Signal(accumulator=SumAccumulator)
        signal.connect(handler_zero)
        signal.connect(handler_one)
        signal.connect(handler_two)
        val = signal.emit()
        self.assertEqual(val, 3)
        del signal

    def test_anyacceptaccumulator(self):
        signal = Signal(accumulator=AnyAcceptAccumulator)
        signal.connect(handler_false)
        signal.connect(handler_zero)
        val = signal.emit()
        self.assertEqual(val, False)

        signal.clear()

        signal.connect(handler_false)
        signal.connect(handler_two)
        signal.connect(handler_zero)
        val = signal.emit()
        self.assertEqual(val, 2)

        del signal

    def test_allacceptaccumulator(self):
        signal = Signal(accumulator=AllAcceptAccumulator)
        signal.connect(handler_one)
        signal.connect(handler_two)
        val = signal.emit()
        self.assertEqual(val, True)

        signal.clear()

        signal.connect(handler_zero)
        signal.connect(handler_two)
        signal.connect(handler_one)
        val = signal.emit()
        self.assertEqual(val, 0)

        del signal

    def test_lastvalueaccumulator(self):
        signal = Signal(accumulator=LastValueAccumulator)
        signal.connect(handler_one)
        signal.connect(handler_two)
        val = signal.emit()
        # Signal don't guarantee the order of execution
        self.assertTrue(val in (1, 2,))

        del signal

    def test_valuelistaccumulator(self):
        signal = Signal(accumulator=ValueListAccumulator)
        signal.connect(handler_one)
        signal.connect(handler_two)
        val = signal.emit()
        val = list(val)
        val.sort()
        self.assertEqual(val, [1, 2, ])

        del signal


if __name__ == '__main__':
    unittest.main()
