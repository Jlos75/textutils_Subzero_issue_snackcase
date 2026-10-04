def word_count(text):
    """Return the number of words in the given text."""
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


def character_count(text):
    """Return the number of characters in the given text."""
    count = 0

    for _ in text:
        count += 1

    return count


def reverse(text):
    """Return the given text reversed."""
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text

def snake_case(text):
    """
    Replace space by underscore in the text
    And all the text is lowercase
    
    Args:
        text (str) : The text
    
    Returns:
        str : The snack case text
    
    """
    text_split = text.split()
    snake_case = "_".join(text_split).lower()
    return(snake_case)
