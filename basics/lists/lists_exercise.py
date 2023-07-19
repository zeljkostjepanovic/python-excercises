#!/usr/bin/env python3
"""This module is used for list excercises."""


def convert(lst):
    """Convert multiple words to list."""
    return ([i for item in lst for i in item.split()])


cities = []

print("Which cities did you visit:")
x = input()

cities.append(x)

for city in convert(cities):
    print('I\'ve visited %s.' % city)
