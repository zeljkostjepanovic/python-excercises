# practice while loops. A naive password input check

def set_password(x):
    pwd = x
    while len(pwd) < 8:
        print("Your password is too short.")
        pwd = input("Enter password: ")
    return pwd
    

set_password("29839")