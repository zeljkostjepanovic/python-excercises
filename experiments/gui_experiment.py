import PySimpleGUI as sg

label1 = sg.Text('Select files to compress')
input1 = sg.Input(key='-IN-', enable_events=True)
choose_button1 = sg.FilesBrowse("Choose", key="-CHOOSE-")

label2 = sg.Text('Select destination folder')
input2 = sg.Input(key='-IN-', enable_events=True)
choose_button2 = sg.FolderBrowse("Choose", key="-CHOOSE-")

compress_button = sg.Button('Compress')

window = sg.Window('Compress', 
                   layout=[[label1, input1, choose_button1], 
                           [label2, input2, choose_button2],
                           [compress_button]])


window.read()
window.close()