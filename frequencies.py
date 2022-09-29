"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] = frequencies[item] + 1
    return frequencies
