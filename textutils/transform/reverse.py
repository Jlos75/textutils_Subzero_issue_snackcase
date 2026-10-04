def reverse(text):
    """Reverse the characters of a text.

    Args:
        text (str): The text to reverse.

    Returns:
        str: A new string containing the characters in reverse order.
    """
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text
