def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): A list of int or float values.

    Returns:
        float or str: The average value or a message if the list is empty.
    """
    if not numbers:  # Safely check if list is empty
        return "No numbers provided."

    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        return "List must contain only numeric values."


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([]) == "No numbers provided."
    assert calculate_average(["a", 10]) == "List must contain only numeric values."
