import PySimpleGUI as sg

text = sg.Text("Welcome")
button = sg.Button("Delete", key="delete")
window = sg.Window('My app', layout=[[text], [button ]])

while True:
    event, values = window.read()
    print(event, values)
    print(window["delete"])