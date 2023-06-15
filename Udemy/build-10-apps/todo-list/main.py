while True:
    user_action = input("Type /add, /show, /edit, /complete or /exit: ").lower().strip()
    
    match user_action:
        case '/add':
            todo = input("Enter a todo: ") + "\n"
            
            with open('todos.txt','r') as file:
                todos = file.readlines()
 
            todos.append(todo)
                      
            with open('todos.txt','w') as file:
                file.writelines(todos)
            
        case '/show':
            with open('todos.txt','r') as file:
                todos = file.readlines()
                          
            for index,item in enumerate(todos, start=1):
                item = item.strip("\n")
                row = f"{index}-{item}"
                print(row)
        case '/edit':
            with open('todos.txt','r') as file:
                todos = file.readlines()
        
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            
            with open('todos.txt','w') as file:
                file.writelines(todos)
                
        case '/complete':
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            for index,item in enumerate(todos, start=1):
                item = item.strip("\n")
                row = f"{index}-{item}"
                print(row)
                
            number = int(input("Which one is completed? "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)         
            
            with open('todos.txt','w') as file:
                file.writelines(todos)    
                
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
            
        case '/exit':
            exit()
        case other:
            print("I didnt' understand that.")
    
print(todos)