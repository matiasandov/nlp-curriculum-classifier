import PySimpleGUI as sg
import processPdf

#prediccion, probabilidad = processPdf.process_response(path)
# percentage = probabilidad * 100
# print(f"{percentage:.1f}%")

sg.theme("DarkTeal2")   # Add a touch of color

# layout de dos columnas

# All the stuff inside your window.
layout = [[sg.T("")],
          [sg.Text('Choose a CV'), sg.Input()],
          [sg.FileBrowse(key="-IN-")],
          [sg.Button('Submit'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Evaluador de CVs', layout, size=(600, 150))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "Submit":
        print(values["-IN-"])

window.close()
