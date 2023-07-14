from modules import functions
import PySimpleGUI as sg
import os

### Make sure to run the program in the same working directory where the script is located
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

label = sg.Text('Type in a task')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button('Add')


window = sg.Window('My TODOS', 
                   layout=[[label], [input_box, add_button]], 
                   font=("Sans", 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()