from modules import functions
import PySimpleGUI as sg

label = sg.Text('Type in a task')
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button('Add')
window = sg.Window('My TODOS', layout=[[label],
                                       [input_box,add_button]])
window.read()
window.close()