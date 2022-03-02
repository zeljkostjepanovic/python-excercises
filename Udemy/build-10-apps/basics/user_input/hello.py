from unicodedata import name


name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
time = "today"

"""Two types of string formatting. Second one works only in Python 3.6+"""
message = "Hello %s %s! What's going on %s?" % (name, surname, time)
messagef36 = f"Hello {name} {surname}! What's going on {time}?"
print(message, messagef36)