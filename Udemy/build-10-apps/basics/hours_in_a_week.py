#!/usr/bin/env python3

def my_function_z(x):
    """Calculate how many hours in the provided number of weeks"""
    if x == 1:
        print('You have', x*(7*24), 'hours in', x, 'week.')
    else:
        print('You have', x*(7*24), 'hours in', x, 'weeks.')


weeks = int(input("How many weeks: "))
my_function_z(weeks)
