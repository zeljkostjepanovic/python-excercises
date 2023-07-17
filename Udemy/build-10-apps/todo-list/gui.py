from modules import functions
import PySimpleGUI as sg
import os

### Make sure to run the program in the same working directory where the script is located
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

label = sg.Text('Type in a task')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])

edit_button = sg.Button('Edit')

window = sg.Window('My TODOS', 
                   layout=[[label], 
                           [input_box, add_button],
                           [list_box,edit_button],
                           [complete_button]], 
                   font=("Sans", 10))

while True:
    event, values = window.read()
    print("1 ", event)
    print("2 ", values)
    print("3 ", values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            if new_todo in todos:
                sg.popup("This task already exists")
            else:
                todos.append(new_todo)
                functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo+"\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
             
        case sg.WIN_CLOSED:
            break


window.close()