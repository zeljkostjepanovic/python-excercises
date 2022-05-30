myfile = open("fruits.txt", "r")
file_content = myfile.read()
myfile.close()

with open("fruits.txt", "r") as myfile:
    content = myfile.read()


print(file_content)
print(content)
