def sample_function_add(a, b):
    """
    This is a sample function which adds a and b

    Args:
        a (int): Number to add
        b (int): Number to add

    Returns:
        int: Addition of a and b

    >>> sample_function_add(1, 2)
    3

    >>> sample_function_add(0, 2)
    Traceback (most recent call last):
        ...
    ValueError: a or b must be greater than 1
    """
    if not a or not b:
        raise ValueError("a or b must be greater than 1")
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
