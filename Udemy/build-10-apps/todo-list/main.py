while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
            
        with open('todos.txt','r') as file:
            todos = file.readlines()
 
        todos.append(todo)
                      
        with open('todos.txt','w') as file:
            file.writelines(todos)
            
    elif user_action.startswith("show"):
        with open('todos.txt','r') as file:
            todos = file.readlines()
                        
        for index,item in enumerate(todos, start=1):
            item = item.strip("\n")
            row = f"{index}-{item}"
            print(row)
            
    elif user_action.startswith("edit"):
        with open('todos.txt','r') as file:
            todos = file.readlines()
    
        for index,item in enumerate(todos, start=1):
            item = item.strip("\n")
            row = f"{index}-{item}"
            print(row)
    
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"
        
        with open('todos.txt','w') as file:
            file.writelines(todos)
                
    elif user_action.startswith("complete"):
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
            
    elif user_action.startswith("exit"):
        break

    else:
        print("Didn't understand that.")

print("Bye!")
exit()