from subscription.signals.accumulators.base import AbstractAccumulator


class NoneAccumulator(AbstractAccumulator):
    """
    An accumulator that never stops emission and sets emission result to
    None. If there are no handlers at all, emission result is None.
    """
    def get_initial_value(self):
        return None

    def accumulate_value(self, accumulated_value, value_to_add):
        return None

    def should_continue(self, accumulated_value):
        return True

    def post_process_value(self, accumulated_value):
        return None


class SumAccumulator(AbstractAccumulator):
    """
    An accumulator that never stops emission and sets emission result to
    sum of all handler returns. If there are no handlers at all, emission
    result is 0.
    """
    def get_initial_value(self):
        return 0

    def accumulate_value(self, accumulated_value, value_to_add):
        try:
            new_value = int(value_to_add)
        except:
            new_value = 0

        return accumulated_value + new_value

    def should_continue(self, accumulated_value):
        return True

    def post_process_value(self, accumulated_value):
        return accumulated_value


class AnyAcceptAccumulator(AbstractAccumulator):
    """
    An accumulator that stops emission if any handler returns a non-zero
    value and sets emission result to it in this case. If all handlers
    return zero values, signal emission is not stopped and result is
    returned by last handler. If there are no handlers at all, emission
    result is False.
    """
    def get_initial_value(self):
        return False

    def accumulate_value(self, accumulated_value, value_to_add):
        return accumulated_value + value_to_add

    def should_continue(self, accumulated_value):
        return accumulated_value == 0

    def post_process_value(self, accumulated_value):
        return accumulated_value


class AllAcceptAccumulator(AbstractAccumulator):
    """
    An accumulator that stops emission if any handler returns a zero
    value and sets emission result to it in this case. If all handlers
    return non-zero values, signal emission is not stopped and result is
    returned by last handler. If there are no handlers at all, emission
    result is True.
    """
    def get_initial_value(self):
        return True

    def accumulate_value(self, accumulated_value, value_to_add):
        return value_to_add if not value_to_add else accumulated_value

    def should_continue(self, accumulated_value):
        return True if accumulated_value else False

    def post_process_value(self, accumulated_value):
        return accumulated_value


class LastValueAccumulator(AbstractAccumulator):
    """
    An accumulator that always returns the value returned by last
    handler. If there are no handlers at all, emission result is None.
    """
    def get_initial_value(self):
        return None

    def accumulate_value(self, accumulated_value, value_to_add):
        return value_to_add

    def should_continue(self, accumulated_value):
        return True

    def post_process_value(self, accumulated_value):
        return accumulated_value


class ValueListAccumulator(AbstractAccumulator):
    """
    An accumulator that returns a list of all handler results. If there
    are no handlers at all, emission result is an empty list.
    """
    def get_initial_value(self):
        return []

    def accumulate_value(self, accumulated_value, value_to_add):
        accumulated_value.append(value_to_add)
        return accumulated_value

    def should_continue(self, accumulated_value):
        return True

    def post_process_value(self, accumulated_value):
        return tuple(accumulated_value)


DefaultAccumulator = NoneAccumulator
