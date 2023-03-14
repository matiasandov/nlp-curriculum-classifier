import PySimpleGUI as sg

sg.theme("DarkTeal2")   # Add a touch of color

# layout de dos columnas

# All the stuff inside your window.
<<<<<<< HEAD
layout = [[sg.T("")],
          [sg.Text('Choose a CV'), sg.Input()],
          [sg.FileBrowse(key="-IN-")],
          [sg.Button('Submit'), sg.Button('Cancel')]]
=======
layout = [  [sg.Text('Selección de Curriculums')],
            [sg.Text('Al subir un CV podrás ')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
>>>>>>> 24128f474865c13b76b11a679a5cf1b897ff27ef

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
