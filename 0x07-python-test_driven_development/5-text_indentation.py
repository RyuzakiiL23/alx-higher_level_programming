#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the input is not a string.
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    text = text.strip()
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            if text[i] != ' ' or (i > 0 and text[i-1] not in ('.', '?', ':')):
                print(text[i], end="")
