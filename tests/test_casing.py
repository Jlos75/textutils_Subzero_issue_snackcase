from textutils.casing import capitalize_words

def test_capitalize_words_basic():
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_empty():
    assert capitalize_words("") == ""

def test_capitalize_words_multiple_spaces():
    assert capitalize_words("hello   world") == "Hello   World"

def test_capitalize_words_tabs():
    assert capitalize_words("hello\tworld") == "Hello\tWorld"