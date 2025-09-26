def calculate_average(*args):
    """
    Calculates the average of a variable number of numeric arguments.

    Parameters:
        *args (float or int): A sequence of numbers to average.

    Returns:
        float: The average of the input numbers.
        None: If no arguments are provided.

    Example:
        >>> calculate_average(10, 20, 30)
        20.0
    """
    if not args:
        return None  # Avoid division by zero

    total = sum(args)
    count = len(args)
    return total / count

print(calculate_average(10, 20, 30))  # Output: 20.0
