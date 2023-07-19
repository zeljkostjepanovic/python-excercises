#!/usr/bin/env python3

mylist = ["something", 2, 3, 4, "list", 10, 89.8]


def extract_int(a_list):
    """
    Extract integers from provided list
    """
    int_list = []
    for i in a_list:
        if isinstance(i, int):
            int_list.append(i)
        else:
            continue
    return int_list


def greater_than_0(a_list):
    """
    Returns only numbers greater than 0
    """
    return [i for i in a_list if i > 0]


def sub_str_with_0(a_list):
    """
    Substitutes strings with 0
    """
    return [0 if isinstance(i, str) else i for i in a_list]


def concat_dec(a_list):
    """
    concatenate decimal numbers from list
    """
    nums = []
    for i in a_list:
        if isinstance(i, float):
            nums.append(i)
        elif isinstance(i, str):
            try:
                nums.append(float(i))
            except ValueError:
                continue
        else:
            continue
    return sum([i for i in nums])

# print(extract_int(mylist))
# print(greater_than_0([0,1,-5,-3,5,100,-100]))
# print(sub_str_with_0(["string", 1, 3, 4, 5, "something here", 89, 99, "29"]))
# print(concat_dec([12.3,34.2,41.892,5,"str", "20", "try this out"]))
