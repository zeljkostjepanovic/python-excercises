#!/usr/bin/env python3
"""This is a module docstring."""
import json
import sys
import logging
from datetime import datetime

data = json.load(open("data.json"))
logging.basicConfig(filename="dict_log.log")


def date_time():
    """Provide current date and time."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H:%M:%S")


def lookup():
    """Try to look up a word in a dictionary file."""
    word = input("Enter a word: ").lower()

    try:
        return data[word]
    except Exception as dict_error:
        print("No definition for your entry.")
        logging.error(date_time(), exc_info=dict_error)
        sys.exit()


print(lookup())
