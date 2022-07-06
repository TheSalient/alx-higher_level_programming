#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """real file."""
    with open("filename", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
