import abc
import threading


class AbstractSignal(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def get_accumulator(self):
        pass

    def __init__(self):
        self.lock = threading.Lock()
        self._handlers = set()

    def connect(self, handler, safe=True):
        """
        Connect ``handler`` to the signal.

        If ``safe`` is True it will connect handler to the signal unless
        it is connected already.
        """
        if not callable(handler):
            return False

        retval = True
        self.lock.acquire()

        try:
            if handler in self._handlers and safe:
                retval = False
            else:
                self._handlers.add(handler)
        finally:
            self.lock.release()

        return retval

    def disconnect(self, handler):
        """Disconnect ``handler`` to the signal."""
        retval = True
        self.lock.acquire()

        try:
            self._handlers.remove(handler)
        except KeyError:
            retval = False
        finally:
            self.lock.release()

        return retval

    def is_connected(self, handler):
        """Determine if ``handler`` is connected to the signal."""
        retval = None
        self.lock.acquire()

        try:
            retval = handler in self._handlers
        finally:
            self.lock.release()

        return retval

    def clear(self):
        """Remove all handlers from the signal."""
        self.lock.acquire()

        try:
            self._handlers.clear()
        finally:
            self.lock.release()

    def count_handlers(self):
        """Get the number of handlers connected to this signal."""
        return len(self._handlers)

    def has_handlers(self):
        """Determine if the signal has any handlers."""
        return len(self._handlers) > 0

    def __call__(self, *args, **kwargs):
        """Same as emit method."""
        return self.emit(*args, **kwargs)

    def emit(self, *args, **kwargs):
        """Invoke handlers connected to self, passing arguments to them."""
        acc = self.get_accumulator()
        acc_value = acc.get_initial_value()

        self.lock.acquire()

        try:
            for handler in self._handlers:
                value = handler(*args, **kwargs)
                acc_value = acc.accumulate_value(acc_value, value)
                if not acc.should_continue(acc_value):
                    break
        finally:
            self.lock.release()

        return acc.post_process_value(acc_value)
