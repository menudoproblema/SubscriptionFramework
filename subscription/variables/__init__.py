import abc


class AbstractVariable(metaclass=abc.ABCMeta):
    def predicate(self, predicate):
        """
        Construct a condition, whose state is always given predicate
        over this variable value.
        """
        pass

    def transform(self, transformer):
        """
        Construct a variable, whose state is always given transformation
        of this variable value.
        """
        pass

    def is_true(self):
        """Identical to predicate (bool)."""
        pass
