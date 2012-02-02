from subscription.signals import Signal


def sum(a, b):
    print ('%d + %d = %d' % (a, b, a + b))


signal = Signal()

signal.connect(sum)
signal(5, 10)
