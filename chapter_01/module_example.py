#!/usr/bin/env python
"""
This script uses the pyjokes library to print a random joke.
"""

import pyjokes

def print_joke():
    """
    Gets a random joke from the pyjokes library and prints it.
    """
    joke_text = pyjokes.get_joke()
    print(joke_text)

if __name__ == "__main__":
    print_joke()