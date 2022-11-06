#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python3 url_reader.py <URL>

    example: python3 url_reader.py 'http://sixty-north.com/c/t.txt'
"""
import sys
from urllib.request import urlopen


def fetchwords(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing a word from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(story_words):
    """Print items one per line

    Args:
        An iterable series of printable items
    """

    for word in story_words:
        print(word)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: the URL of a UTF-8 text document.
    """
    words = fetchwords(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1])
