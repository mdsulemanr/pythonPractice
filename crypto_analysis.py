from collections import Counter
import string

def freq_analysis(message: str):
    """
    Perform frequency analysis on a given lowercase message.

    Args:
        message (str): The input text containing only lowercase letters a–z.

    Returns:
        list[float]: A list of normalized frequencies for each letter a–z.
    """
    if not message:
        return [0.0] * 26  # Avoid division by zero

    counts = Counter(message)
    total = len(message)

    return [counts.get(letter, 0) / total for letter in string.ascii_lowercase]

print(freq_analysis("abcd"))
# [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis("adca"))
# [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis('bewarethebunnies'))
# [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
