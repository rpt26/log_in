#!/usr/bin/env python3

import PySimpleGUI as sg
import time
import os

log_file_name = '/home/msm-class/attendance_log.csv'


#ensure the expected header lines are there:
if not os.path.isfile(log_file_name):
    with open(log_file_name,'wt') as f:
        f.write('mifare_id,datetime\n')

# Jankily check the header
with open(log_file_name,'rt') as f:
    lines = f.readlines()

if len(lines) >= 1:
    line = lines[0].strip()
else:
    line = ''

# add the header if it is not there
if line != 'mifare_id,datetime':
    lines = ['mifare_id,datetime\n'] + lines
    with open(log_file_name,'wt') as f:
        f.writelines(lines)

#set up the GUI

# Define the window's contents
layout = [[sg.Image('MaterialscienceCOL.png',
                    background_color='white')],
          #[sg.Text("Swipe your card to record attendance:",
          #         text_color='black',
          #         background_color='white')],
          [sg.Input(key='-INPUT-', do_not_clear=False,visible=True)],
          [sg.Text('Ready', size=(40,1),
                   key='-TIME-',
                   text_color='blue',
                   background_color='white')],
          [sg.Text("Swipe below",
                   font=('bold', 20),
                   text_color='black',
                   background_color='white')],
          [sg.Image('down_arrow.png',
                    background_color='white')],
          [sg.Button(bind_return_key=True,
                     visible=False)]
          ]


width, height = sg.Window.get_screen_size()

# Create the window
window = sg.Window('Materials Science Swipe In',
                   layout,
                   margins=(10,10),
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
