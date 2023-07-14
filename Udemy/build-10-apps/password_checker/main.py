import string

password = input("Enter a password to check: ")

def test_length(a):
    if len(password) > 12 :
        return "Pass"
    else:
        return "Fail"

def test_upper_lower(a):
    results = []
    for char in a:
        if char.isupper():
            results.append("upper")
        elif char.islower():
            results.append("lower")
        else:
            pass
    if all([x in results for x in ["lower","upper"]]):
        return "Pass"
    else:
        return "Fail"

def test_spec_char(a):
    if any([x in a for x in set(string.punctuation.replace("_",""))]):
        return "Pass"
    else:
        return "Fail"

def has_digits(a):
    results = []
    for char in a:
        if char.isdigit():
            results.append("digit")
        else:
            results.append("nodigit")
    if all([x in results for x in ["digit","nodigit"] ]):
        return "Pass"
    else:
        return "Fail"
    
if test_length(password) == "Pass" and test_upper_lower(password) == "Pass" and test_spec_char(password) == "Pass" and has_digits(password) == "Pass":
    print("Your password is STRONK! Well Done!")
else:
    print("Your password is WEAK... try AGAIN!")
    print()
