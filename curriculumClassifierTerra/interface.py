import PySimpleGUI as sg
import processPdf

#prediccion, probabilidad = processPdf.process_response(path)
# percentage = probabilidad * 100
# print(f"{percentage:.1f}%")

sg.theme("DarkTeal2")   # Add a touch of color

# layout de dos columnas

# All the stuff inside your window.
layout = [[sg.T("Seleccionar curriculum para predecir si es considerado o no ", font=('Helvetica', 20))],
          [sg.Text('Choose a CV'), sg.Input()],
          [sg.FileBrowse(key="-IN-")],
          [sg.Button('Submit')]]

# Create the Window
window = sg.Window('Evaluador de CVs', layout, size=(1000, 350))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "Submit":
        prediccion, probabilidad = processPdf.process_response(values["-IN-"])
        #print(values["-IN-"])
        percentage = probabilidad * 100
        print(f"{percentage:.1f}%")
        layout= [
            [sg.Text("Resultados para el archivo seleccionado", font=('Helvetica', 32))],
            [sg.Text("Archivo: ")],
            [sg.Text(values["-IN-"])],
            [sg.Text("Predicción de aceptación: ")],
            [sg.Text(prediccion)],
            [sg.Text("Probabilidad: ")],
            [sg.Text(f"{percentage:.1f}%")],
            [sg.Button('Cancel')]
        ]
        window.close()
        window = sg.Window('Evaluador de CVs', layout, size=(1000, 350))

window.close()


