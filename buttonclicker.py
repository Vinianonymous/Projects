import PySimpleGUI as sg

# All the stuff inside your window.
layout = [ 
            [sg.Text('Insert username'), sg.InputText(key="user")],
            [sg.Text('Insert Password'), sg.InputText(key="pass")],
            [sg.Button('Log on'), sg.Button('Cancel'), sg.Button('Sign in')], 
            [sg.Text(key="error")]
        ]
username = ""
password = ""

# Create the Window
window = sg.Window('Login', layout)

#Proceed function
def proceed():
    buttonregister = 0
    print("Function sucessfuly initiated")
    layout = [[sg.Button("Press me!"), sg.Text('Button Presses:'), sg.Text(key='-BUTTON_PRESSES-')],
              [sg.Button("Exit :(")]
              ]
    window = sg.Window('Arrival', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit :(":
            break
        if event == "Press me!":
            buttonregister += 1
            print(f"Presses: {buttonregister}")
            window['-BUTTON_PRESSES-'].update(buttonregister)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Sign in':
        if (window["user"] != "" and window["pass"] != ""):
            username = window["user"]
            password = window["pass"]
            window["user"].update("")
            window["pass"].update("")
            print("Registry successful, log on now")
        else:
            window["error"].update("Please insert a valid username and password.")
    
    if event == 'Log on':
        if (window["user"] != username or window["pass"] != password):
            print("Incorrect password/username.")
        else:
            print("Welcome!")
            proceed()
            window.close()
window.close()