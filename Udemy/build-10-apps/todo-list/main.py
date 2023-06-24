import os

### Make sure to run the program in the same working directory where the script is located
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

def get_todos(filepath='todos.txt'):
    """ Read a text file and return list of todos

    Args:
        filepath (string): path of the text file with saved todos,
        with each todo in a separate line

    Returns:
        list: returns a list of strings (todos)
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(filepath,content):
    """ Write a list of todos to a file

    Args:
        filepath (string): Path of the file where todos are saved
        content (list): List of todos to write to file, one line for each
    """
    with open(filepath, 'w') as file:
        file.writelines(content)

### Main loop
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
            
        todos = get_todos()
        
        if len(todo) > 1:
            todos.append(todo)
            write_todos("todos.txt",todos)              
        else:
           print("Empty task?")
           continue
            
    elif user_action.startswith("show"):
        todos = get_todos()
                        
        for index,item in enumerate(todos, start=1):
            item = item.strip("\n")
            row = f"{index}-{item}"
            print(row)
            
    elif user_action.startswith("edit"):
        try:
            todos = get_todos()
        
            for index,item in enumerate(todos, start=1):
                item = item.strip("\n")
                row = f"{index}-{item}"
                print(row)
        
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            
            write_todos("todos.txt",todos)
        except:
            print("Try again.")
            continue
        
    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            
            for index,item in enumerate(todos, start=1):
                item = item.strip("\n")
                row = f"{index}-{item}"
                print(row)
                
            number = int(input("Which one is completed? "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)         
                
            write_todos("todos.txt",todos)   
                
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except:
            print("Command not valid, try again.")
            continue
        
    elif user_action.startswith("exit"):
        break

    else:
        print("Didn't understand that.")

print("Bye!")
exit()