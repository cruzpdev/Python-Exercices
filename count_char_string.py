def count_chars(s):
    """
    Count the number of occurrences of each character in a string.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary where the keys are the characters in the string
        and the values are the number of occurrences of each character.
    """
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

# Example usage:
print(count_chars("aba"))  # {'a': 2, 'b': 1}
print(count_chars(""))     # {}
