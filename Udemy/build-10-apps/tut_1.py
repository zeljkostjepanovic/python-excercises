#!/usr/bin/env python2

"""
This is a doc string that explains this module.

This is another line for docstring.
I think I'll need to disable this mdule, it's asking too much.
"""

print("Hello world!")

HELLO_STR = "Hello world, this is a string "
HELLO_INT = 21
HELLO_TUPLE = (21, 32)
HELLO_LIST = ["Hello,", "this", "is", "a", "list"]
HELLO_DICT = {"first name": "Zeljko",
              "last name": "Stjepanovic",
              "year born": "1981",
              "eye color": "brown",
              "married": "yes"}

print(HELLO_STR)
print(HELLO_INT)
print(str(HELLO_TUPLE[0]))
print(HELLO_LIST)
print(HELLO_DICT)
print(HELLO_LIST[4])

HELLO_LIST[4] += "!"
print(HELLO_LIST[4])

print(
    HELLO_DICT["first name"] + " " + HELLO_DICT["last name"] + " has " +
    HELLO_DICT["eye color"] + " eyes."
    )
