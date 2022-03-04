colors = [1,2,3,4,5.6,6,7.33,3,4344,5.345,345,545,34,223,77,54,33,12,4,5]

# iterate and print every element from the list
for color in colors:
    print(color)


# iterate and print if the element is more than 50
for color in colors:
    if color > 50:
        print(color)
    else:
        continue

# iterate and print if the element is an integer
for color in colors:
    if type(color) == int:
        print(color)
    else:
        continue


# iterate and print if the element is an integer and more than 50
for color in colors:
    if type(color) == int and color > 50:
        print(color)
    else:
        continue