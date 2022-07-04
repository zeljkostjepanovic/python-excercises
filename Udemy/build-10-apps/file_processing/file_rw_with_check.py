import time
import os

os.chdir(os.getcwd())


while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as vegies:
            print(vegies.read())
    else:
        print("File does not exist")
        exit(1)
    time.sleep(10)  