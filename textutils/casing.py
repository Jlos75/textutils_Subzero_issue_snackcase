def capitalize_words(text):
    """Return the text with the first letter of each word capitalized."""
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