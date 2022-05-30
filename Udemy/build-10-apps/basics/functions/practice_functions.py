def mean(mylist):
    """Calculate the average"""
    return sum(mylist) / len(mylist)


print(mean([1, 3, 4, 5, 3, 56, 6, 3, 2, 334, 2, 3, 445]))


def calculate_length(lst):
    """Return the lenght of the list."""
    return len(lst)

print(calculate_length([7,4,3,4,5]))

def squared(x):
    """Return the number squared, with decimals."""
    return float(x)**2

print(squared(3.23))

def ounce_to_ml(x):
    """Convert ounce to mililiters."""
    return float(x*29.57353)


print(ounce_to_ml(3))

def cels_to_kelvin(x):
    """Convert celsius to kelvin."""
    return x + 273.15

print(cels_to_kelvin(17.5))

monday_temps = [3,4.5,12,16]

for temp in monday_temps:
    print(cels_to_kelvin(temp))


def concat_str(a, b):
    return a + b

print(concat_str("something", "else"))
