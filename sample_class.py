class SampleClass:
    """Sample Class for demonstration"""

    @staticmethod
    def func_concat(a, b):
        """
        This is a sample function which concatenates a and b

        Args:
            a (str): Prefix of string
            b (str): Suffix of string

        Returns:
            str: Combined result of a and b
        """
        return a + b

    @staticmethod
    def func_add(a, b):
        """
        This is a sample function which adds a and b

        Args:
            a (int): Number to add
            b (int): Number to add

        Returns:
            int: Addition of a and b
        """
        return a + b

    @staticmethod
    def func_subtract(a, b):
        """
        This is a sample function which subtracts b from a

        Args:
            a (int): Number to subtract from
            b (int): Number to subtract

        Returns:
            int: Subtraction of b from a
        """
        return a - b
