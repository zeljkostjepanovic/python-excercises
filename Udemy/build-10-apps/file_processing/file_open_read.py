import time

myfile = open("files/fruits.txt", "r")
file_content = myfile.read()
myfile.close()

# Another way to open (and close) file for reading
with open("files/fruits.txt", "r") as myfile:
    content = myfile.read()

while True:
    time.sleep(5)
    print(content)
