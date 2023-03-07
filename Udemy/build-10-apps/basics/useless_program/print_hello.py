
country = input("Where are you from? Or type 'quit' ").lower()

match country:
    case 'usa':
        print("Hello!")
    case 'india':
        print("Namaste!")
    case 'germany':
        print("Hallo!")
    case other:
        print("Don't know that one.")
