coin_flips = []

while True:
    
    coin_toss = input("Throw the coin and enter 'head' or 'tail'. To terminate, type 'exit'.  ")
    
    if coin_toss == "exit":
        break
    
    elif coin_toss in ("tail","head"):
        coin_flips.append(coin_toss)
        heads = coin_flips.count("head")
        tails = coin_flips.count("tail")
        heads_percent = round((heads / (heads+tails)) * 100, 2)
        print(f"Percentage of heads: {heads_percent}")
        
        with open('coin_toss_record.txt', 'a+') as file:
            for toss in coin_flips:
                file.write(toss + "\n")
            
    else:
        print("Please enter head or tail.")
    
    

heads = coin_flips.count("head")
tails = coin_flips.count("tail")

try: 
    tails_percent = round((tails / (heads+tails)) * 100, 2)
    heads_percent = round((heads / (heads+tails)) * 100, 2)
    
    print(f"All coin tosses: {heads + tails}")
    print(f"There were {heads} heads.")
    print(f"There were {tails} tails.")
    print(f"Percentage of tails: {tails_percent}")
    print(f"Percentage of heads: {heads_percent}")
except ZeroDivisionError:
    print("Can't divide by 0, terminating.")