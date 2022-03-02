from tabnanny import check


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


def blah(x,array):
    """Check if value in array, both provided as arguments to this function"""
    if x in array:
        return "True"
    else:
        return "False"

print(blah(1,[1,2,3]))
print(blah(1,['1',2,3]))
print(blah(1,[2,3]))

def checkpasslength(value):
    """Check string length."""
    if len(value) >= 8:
        return True
    else:
        return False


print(checkpasslength("thepass"))
print(checkpasslength("ThisismypasswordNOT"))


def tempcheck(x):
    if x > 7:
        return "Warm"
    else:
        return "Cold"

print(tempcheck(5))
print(tempcheck(7))
print(tempcheck(10))