def word_count(text):
    """Count the number of words in a text.

    Words are separated by spaces, tabs, or newline characters.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words contained in the text.
    """
    count = 0
    in_word = False

    for char in text:
        if char != " " and char != "\n" and char != "\t":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count
