def mean_func(x):
    """Calculate mean for a list of values or dictionary values."""
    if type(x) == list:
        return sum(x) / len(x)
    elif type(x) == dict:
        return sum(x.values()) / len(x)
    else:
        print("Please provide a list with numerical values, or a dictionary with numerical values.")
        return TypeError


student_grades = {"Mary":5,"John":8,"Greg":10,"Lisa":10,"Michael":6}

print(mean_func([12,3,2,34,4,3,2]))
print(mean_func(student_grades))
print(mean_func("Rocky 3"))