import PySimpleGUI as sg
import processPdf

# layout de dos columnas

# All the stuff inside your window.
layout = [
            [sg.T("Seleccionar curriculum para predecir si es considerado o no ", font=('Helvetica', 20))],
            [sg.Text('Choose a CV', font=('Helvetica', 14))], 
            [sg.Input(key= "-INPUT-", font=('Helvetica', 12))],
            [sg.FileBrowse(key="-IN-", font=('Helvetica', 12), button_color=('dark slate gray', '#FFFFFF'))],
            [sg.Button('Submit', font=('Helvetica', 12), button_color=('dark slate gray', '#FFFFFF')), 
           sg.Button('Cancel', font=('Helvetica', 12), button_color=('dark slate gray', '#FFFFFF'))]
        ]

# Create the Window
background_color= '#f2f2f2'
window = sg.Window('Evaluador de CVs', layout, size=(1000, 350))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "Submit":
        #no considerado es 1
        #(0.9365207, 1)
        probabilidad, prediccion = processPdf.process_response(values["-IN-"])
        #print(values["-IN-"])
        percentage = probabilidad * 100
        
        if prediccion == 1:
            prediccion = 'No considerado'
        else:
            prediccion = 'Considerado para siguiente entrevista'
        
        layout= [
            [sg.Text("Resultados para el archivo seleccionado", font=('Helvetica', 32))],
            [sg.Text("Archivo: ", font=('Helvetica', 14))],
            [sg.Text(values["-IN-"], font=('Helvetica', 13))],
            [sg.Text("Predicción de aceptación: ", font=('Helvetica', 14))],
            [sg.Text(prediccion, font=('Helvetica', 13))], 
            [sg.Text("Probabilidad: ", font=('Helvetica', 14))],
            [sg.Text(f"{percentage:.1f}%", font=('Helvetica', 13))],
            [sg.Button('Cancel', font=('Helvetica', 12), button_color=('dark slate gray', '#FFFFFF'))]
        ]
        window.close()
        window = sg.Window('Evaluador de CVs', layout, size=(1000, 350))
        #print(f"{percentage:.1f}%")

window.close()