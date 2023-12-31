#!/usr/bin/env python3

import PySimpleGUI as sg
import time
import os

log_file_name = '/home/msm-class/attendance_log.csv'

# Set up the GUI
# Define the window's contents
layout = [[sg.Image('MaterialscienceCOL.png',
                    background_color='white',pad=5)],
          #[sg.Text("Swipe your card to record attendance:",
          #         text_color='black',
          #         background_color='white')],
          [sg.Input(key='-INPUT-', do_not_clear=False,visible=True,pad=5)],
          [sg.Text('Ready', size=(40,1), font=(16),
                   key='-TIME-',
                   text_color='blue',
                   background_color='white',pad=5)],
          [sg.Text("Swipe below",
                   font=('bold', 20),
                   text_color='black',
                   background_color='white',pad=5)],
          [sg.Image('down_arrow.png',
                    background_color='white',pad=5)],
          [sg.Button(bind_return_key=True,
                     visible=False)]
          ]


width, height = sg.Window.get_screen_size()

# Create the window
window = sg.Window('Materials Science Swipe In',
                   layout,
                   margins=(10,50), #left/right, top/bottom
                   #disable_minimize=True,
                   #disable_close=False,
                   text_justification='center',
                   #keep_on_top=True,
                   #modal=True,
                   element_justification='center',
                   finalize=True,
                   background_color='white',
                   size=(800,480))
window.maximize()

window.TKroot["cursor"] = "none"



n = 0
colours = ['red','darkorange','yellow4','green','blue','indigo']
# start a counter and a series of colours to rotate around to make it clearer that the
# confirmation message has changed

# Display and interact with the Window using an Event Loop
while True:
    
    event, values = window.read()
    n += 1
    
    # determine the input ID:
    identity = values['-INPUT-']
    
    # briefly clear the confirmation text to provide 
    # more affirmative feedback
    window['-TIME-'].update('   ')
    window.refresh()
    time.sleep(0.1)
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit' or values['-INPUT-'] == 'quit':
        break
    
    # Output a message confirming the time of recording to the window
    
    window['-TIME-'].update('Attendance recorded: ' + time.ctime(),
                            text_color=colours[n % 6])
    
     # record the ID and the time to a file   
    with open(log_file_name,'at') as f:
        f.write(identity + ',' + time.ctime() + '\n')

# Finish up by removing from the screen
window.close()
