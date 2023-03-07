todos = []

# while True:
#     task = input("What do you want to do today? ")
#     print("Type 'break' to end taks list.")
#     if task == "break":
#         break
#     else:
#         print(task.capitalize())
#         tasks.append(task)

while True:
    user_action = input("Type add, show or exit: ").lower().strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for i in enumerate(todos, start=1):
                print(i[0],i[1])
        case 'exit':
            exit()
        case other:
            print("I didnt' understand that.")
    
print(todos)
