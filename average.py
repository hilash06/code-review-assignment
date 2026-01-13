def average(numbers: list[float]) -> float:
    """
    Calculates the average of a list of numbers.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)
