from subscription.signals import Signal
from subscription.signals.accumulators import SumAccumulator

def handler1(param):
    print('Handler1:', param)
    return 1

def handler2(param):
    print('Handler2:', param)
    return 2

mysignal = Signal()
mysignal.connect(handler1)

print('Emit')
val = mysignal.emit(1)
print('Return value:', val) # Must be 'None'

print('Emit')
mysignal.connect(handler2)
mysignal.emit(2)

print('Emit')
mysignal.disconnect(handler1)
mysignal.emit(3)

print('Emit')
mysignal.connect(handler1)
mysignal.connect(handler1)
mysignal.disconnect(handler2)
mysignal.connect(handler2)
mysignal.emit(4)

print('Emit')
mysignal.clear()
mysignal.emit(5)


print('Sum accumulator')
mysignal = Signal(accumulator=SumAccumulator())
mysignal.connect(handler1)
mysignal.connect(handler2)
val = mysignal.emit('sum')
print('Return value:', val) # Must be sum of all handlers
