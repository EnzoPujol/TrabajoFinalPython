#!/usr/bin/env python
import string
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   Button
#   Dictionary return values
#   Update of elements in form (Text, Input)
#   do_not_clear of Input elements



layout = [[sg.Text('Enter Your Passcode')],
          [sg.Input(size=(10, 1), do_not_clear=True, key='input')],
          [sg.Button('A', button_color = ('white', 'green')), sg.Button('Y'), sg.Button('Z'), sg.Button('F')],
          [sg.Button('B'), sg.Button('T'), sg.Button('H')],
          [sg.Button('C'), sg.Button('S'), sg.Button('K')],
          [sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')],
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')],
          ]

window = sg.Window('Keypad', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False).Layout(layout)

# Loop forever reading the form's values, updating the Input field
keys_entered = ''
while True:
    event, values = window.Read()  # read the form
    if event is None:  # if the X button clicked, just exit
        break
    if event == 'Clear':  # clear keys if clear button
        keys_entered = ''
    elif event in string.ascii_uppercase:
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += event  # add the new digit
    elif event == 'Submit':
        keys_entered = values['input']
        window.FindElement('out').Update(keys_entered)  # output the final string

    window.FindElement('input').Update(keys_entered)  # change the form to reflect current key string
