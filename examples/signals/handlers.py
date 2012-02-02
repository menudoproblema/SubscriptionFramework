from subscription.signals import Signal


def note(object):
    print('emitted with %s' % object)


signal = Signal()

signal.connect(note)
signal('foo')

signal.disconnect(note)
signal('bar')
