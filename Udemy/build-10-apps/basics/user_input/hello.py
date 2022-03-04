firstname = input("Please enter your name: ")
surname = input("Please enter your surname: ")
time = "today"

"""Two types of string formatting. Second one works only in Python 3.6+"""
message = "Hello %s %s! What's going on %s?" % (firstname, surname, time)
message3 = "Hello {} {}! What's going on {}?".format(firstname, surname, time)
messagef36 = f"Hello {firstname} {surname}! What's going on {time}?"
print(message)
print(message3)
print(messagef36)