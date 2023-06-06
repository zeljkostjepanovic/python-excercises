while True:
    user_action = input("Type /add, /show, /edit, /complete or /exit: ").lower().strip()
    
    match user_action:
        case '/add':
            todo = input("Enter a todo: ") + "\n"
            
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case '/show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            
            new_todos = [item.strip('\n') for item in todos]
                        
            for index,item in enumerate(new_todos, start=1):
                row = f"{index}-{item}"
                print(row)
        case '/edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case '/complete':
            for index,item in enumerate(todos, start=1):
                row = f"{index}-{item}"
                print(row)
            number = int(input("Which one is completed? "))
            todos.pop(number-1)             
        case '/exit':
            exit()
        case other:
            print("I didnt' understand that.")
    
print(todos)