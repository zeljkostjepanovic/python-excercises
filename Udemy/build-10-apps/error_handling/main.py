def divide(a,b):
    try:
        return float(a)/float(b)
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except ValueError:
        return "Please enter numbers for a and b."

a = input("Enter a: ")
b = input("Enter b: ")
print(divide(a,b))

