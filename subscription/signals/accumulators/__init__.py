from subscription.signals.accumulators.base import AbstractAccumulator


class NoneAccumulator(AbstractAccumulator):
    """
    An accumulator that never stops emission and sets emission result to
    None. If there are no handlers at all, emission result is None.
    """
    def get_initial_value(self):
        """Get initial value for this accumulator."""
        return None

    def accumulate_value(self, accumulated_value, value_to_add):
        """Accumulate value_to_add into accumulated_value and return the result."""
        return None

    def should_continue(self, accumulated_value):
        """Examine accumulated_value and decide if signal emission should continue."""
        return True

    def post_process_value(self, accumulated_value):
        """Post-process accumulated_value and return new value."""
        return None