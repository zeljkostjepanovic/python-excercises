def tempcheck(x):
    if x > 25:
        return "Hot"
    elif x >= 15 and x <= 25:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Please enter temperature: "))
print(tempcheck(user_input))