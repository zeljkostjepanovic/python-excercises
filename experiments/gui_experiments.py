import PySimpleGUI as sg
from functions import parser_func

    
feet_label = sg.Text("Feet")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Inches")   
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
result_label = sg.Text("")

layout = [[feet_label, feet_input],[inches_label, inches_input],[convert_button,result_label]]

window = sg.Window("Feet to Meters", layout=layout)

while True:
    event, values = window.read() # type: ignore
    if event == "Convert":
        try:
            feet = float(values["feet"])
            inches = float(values["inches"])
            meters = str(parser_func.convert(feet, inches)) + "m"
            result_label.update(meters)
            window.refresh()
        except ValueError as e:
            result_label.update(f"Invalid Input:{e}")
            window.refresh()
            
    elif event == sg.WIN_CLOSED:
        break
    