# def mean(mylist):
#     """Calculate the average"""
#     return sum(mylist) / len(mylist)


# # print(mean([1, 3, 4, 5, 3, 56, 6, 3, 2, 334, 2, 3, 445]))


# def calculate_length(lst):
#     """Return the lenght of the list."""
#     return len(lst)

# # print(calculate_length([7,4,3,4,5]))

# def squared(x):
#     """Return the number squared, with decimals."""
#     return float(x)**2

# # print(squared(3.23))

# def ounce_to_ml(x):
#     """Convert ounce to mililiters."""
#     return float(x*29.57353)


# print(ounce_to_ml(3))

# def cels_to_kelvin(x):
#     """Convert celsius to kelvin."""
#     return x + 273.15

# print(cels_to_kelvin(17.5))

# monday_temps = [3,4.5,12,16]

# for temp in monday_temps:
    # print(cels_to_kelvin(temp))


# def concat_str(a, b):
#     return a + b

from parser_func import parse, convert
        
feet_inches = input("Enter feet and inches: ")


parsed = parse(feet_inches)
result = convert(parsed['feet'],parsed['inches'])

print(result)

# def get_nr_items(list_of_strings):
#     newlist = list(list_of_strings.split(","))
#     return newlist


# print(get_nr_items('apple,banana,orange'))

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
    
    
# time = calculate_time(1000)
# print(time)