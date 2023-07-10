import random

try: 
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
except ValueError as e:
    print("Please enter numbers, first lower then upper boundary.")
    print(f"{e}")
    exit(1)
    
try:
    print(random.randint(lower_bound,upper_bound))
except Exception as e:
    print(f"something went wrong: {e}")