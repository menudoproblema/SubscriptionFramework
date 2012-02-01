import abc


class AbstractAccumulator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_initial_value(self):
        """Get initial value for this accumulator."""
        pass

    @abc.abstractmethod
    def accumulate_value(self, accumulated_value, value_to_add):
        """Accumulate value_to_add into accumulated_value and return the result."""
        pass

    @abc.abstractmethod
    def should_continue(self, accumulated_value):
        """Examine accumulated_value and decide if signal emission should continue."""
        pass

    @abc.abstractmethod
    def post_process_value(self, accumulated_value):
        """Post-process accumulated_value and return new value."""
        pass
