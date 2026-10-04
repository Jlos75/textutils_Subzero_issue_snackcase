def character_count(text):
    """Count the number of characters in a text.

    Args:
        text (str): The text whose characters will be counted.

    Returns:
        int: The total number of characters in the text.
    """
    count = 0

    for _ in text:
        count += 1

    return count
