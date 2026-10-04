def capitalize_words(text):
    """Capitalize the first letter of each word in a text.

    Words are separated by spaces, tabs, or newline characters.

    Args:
        text (str): The text whose words will be capitalized.

    Returns:
        str: The text with the first lowercase ASCII letter of each
        word converted to uppercase.
    """
    result = ""
    capitalize_next = True

    for char in text:
        if char == " " or char == "\n" or char == "\t":
            result += char
            capitalize_next = True
        elif capitalize_next:
            if "a" <= char <= "z":
                result += chr(ord(char) - 32)
            else:
                result += char

            capitalize_next = False
        else:
            result += char

    return result
