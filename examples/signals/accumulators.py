from subscription.signals import Signal
from subscription.signals.accumulators import AllAcceptAccumulator


def only_even (number):
    return number % 2 == 0


def only_positive (number):
    return number > 0


def not_some (number):
    return number not in (-2, 5, 6, 7, 8, 15)


is_fine = Signal(accumulator=AllAcceptAccumulator)
is_fine.connect(only_even)
is_fine.connect(only_positive)
is_fine.connect(not_some)

print('%d is fine: %s' % (-10, is_fine(-10)))
print('%d is fine: %s' % (4, is_fine(4)))
print('%d is fine: %s' % (7, is_fine(7)))
print('%d is fine: %s' % (8, is_fine(8)))
print('%d is fine: %s' % (20, is_fine(20)))
