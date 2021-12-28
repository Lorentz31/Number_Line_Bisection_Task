'''
cd Desktop
python Number_Line_Bisection_Task_Pilot.1.1.py
Python 3.8.8, pygame 2.1.0, psychopy 2021.2.3
'''

# Importing many important modules
import os
from datetime import datetime
from psychopy import logging, visual, core, event, clock, gui
import numpy as np
from random import randint, sample, random
import pandas as pd

# Clear the command output / set the logging to critical
os.system('cls' if os.name == 'nt' else 'clear')
logging.console.setLevel(logging.CRITICAL)
print('************************************************')
print('"NUMBERS" LINE BISECTION TASK: version alpha')
print('************************************************')
print(datetime.now())
print('************************************************')

# Create length loop / no_trials
no_lengths = 5 # This is the number of lengths (5 lengths)
line_length_array = [] # Set of different line lengths. To append later

# Create number intervals
zeroten = (0, 10)
zerohundred = (0, 100)
hundredtwohund = (100, 200)
tenzero = (10, 0) # Reversed
hundredzero = (100, 0) # Reversed
twohundhundred = (200, 100) # Reversed
nonum = ('nonum') # No number interval

numbers_interval_array = [] # Set of different number intervals (flankers). To append later.
number_requested_array = [] # Set of different trial demands. To append later.
real_value_array = [] # Set of different real values relative to task demands. To append later.


for l in range(0, no_lengths):
    for n in range(0, 7):
        for v in range(0, 3):
            if l == 0: # Create equally-spaced distribution for all lengths
                line_length_array.append(96) # Measures are in pixels
            if l == 1:
                line_length_array.append(128)
            if l == 2:
                line_length_array.append(224)
            if l == 3:
                line_length_array.append(321)
            if l == 4:
                line_length_array.append(48)
            if n == 5: # Create equally-spaced distribution for all number intervals
                numbers_interval_array.append(zeroten)
            if n == 1:
                numbers_interval_array.append(zerohundred)
            if n == 2:
                numbers_interval_array.append(hundredtwohund)
            if n == 3:
                numbers_interval_array.append(tenzero)
            if n == 4:
                numbers_interval_array.append(hundredzero)
            if n == 5:
                numbers_interval_array.append(twohundhundred)
            if n == 6:
                numbers_interval_array.append(nonum)
            if v == 0: # Create equally-spaced distribution for all trial demands
                number_requested_array.append('FIRST THIRD')
            if v == 1:
                number_requested_array.append('MID')
            if v == 2:
                number_requested_array.append('SECOND THIRD')

# Create a pandas dataframe
conditions = pd.DataFrame({'Length': line_length_array,
                            'Interval': numbers_interval_array,
                            'Request': number_requested_array})
conditions = np.array(conditions) # Re-convert in numpy array for further elaboration

# Create real values matrix (measures in pixels) relative to task demand and number interval orientation
for l in range(0, len(line_length_array)):
        if conditions[l][2] == 'FIRST THIRD':
            if conditions[l][1] == zeroten or conditions[l][1] == zerohundred or conditions[l][1] == hundredtwohund or conditions[l][1] == nonum:
                real_value_array.append('%.4f'%((-(conditions[l][0])/6)))
            else:
                real_value_array.append('%.4f'%((-(-(conditions[l][0])/6))))
        if conditions[l][2] == 'SECOND THIRD':
            if conditions[l][1] == tenzero or conditions[l][1] == hundredzero or conditions[l][1] == twohundhundred or conditions[l][1] == nonum:
                real_value_array.append('%.4f'%((-(conditions[l][0])/6)))
            else:
                real_value_array.append('%.4f'%((-(-(conditions[l][0])/6))))
        if conditions[l][2] == 'MID':
            real_value_array.append(0)

# Create a pandas dataframe
conditions = pd.DataFrame({'Length': line_length_array,
                            'Interval': numbers_interval_array,
                            'Request': number_requested_array,
                            'Real Value': real_value_array})
conditions_random = conditions.sample(frac=1) # Randomize trials (for each (5) length there are degrees (4), everything repeated two times (5 x 4 x 2 = 40))
conditions_random = np.array(conditions_random) # Re-convert in numpy array for further elaboration

# Define variables to declare
click_pos = [] # The subjects'mouse click in every trial (in pixels). To append later
trial_no_array = [] # Number of total trials
sub_id_array = [] # To append later
date_value_array = [] # To append later
date_val = datetime.now().strftime('%d%m%Y')
time_value_array = [] # To append later
final_line_length_array = [] # The real sequence of lengths used by the loop. To append later
final_numbers_interval_array = [] # The real sequence of intervals used by the loop. To append later
final_number_requested_array = [] # The real sequence of trial requests used by the loop. To append later
final_real_value_array = [] # The real sequence of actial values used by the loop. To append later
response_latency = [] # To append later

# Setup our experiment
myDlg = gui.Dlg(title = '"Numbers" Line Bisection task (version: alpha)') # The dialog window poping when experiment opens
myDlg.addText('Subject Info')
myDlg.addField('Exp Date', date_val)
myDlg.addField('Number:')
myDlg.addField('Sex:', choices = ['Male', 'Female', 'Prefer not to say'])
myDlg.addField('Age:')
show_dlg = myDlg.show()

if myDlg.OK: # Create the file name
    print(show_dlg)
    save_file_name = show_dlg[0] + '_' + show_dlg[1] + '_number_line_bisection_task.csv'
    print(save_file_name)

else:
    print('user cancelled')

# Create a save filepath (GUI)
save_path = gui.fileSaveDlg(initFileName = save_file_name, prompt = 'Select Save File')

print('Output form save dialog')
print(save_path)

if save_path == None:
    print('Experiment must be saved first')
    core.quit()

# Create window
win0 = visual.Window(size=(1920,1080),
                    color=(0,0,0),
                    fullscr=True,
                    monitor='testMonitor',
                    screen=1,
                    allowGUI=True,
                    pos=(0,0),
                    units='pix')

# Create mouse input
mymouse = event.Mouse(win=win0)

# Create fixation cross
def fixation_cross():
    fix_cross_horiz = visual.Rect(win0,
                                  width = 15,
                                  height = 1.5,
                                  units = 'pix',
                                  lineColor = [-1,-1,-1],
                                  fillColor = [-1,-1,-1],
                                  pos = (0,0))
    fix_cross_vert = visual.Rect(win0,
                                 width = 1.5,
                                 height = 15,
                                 units = 'pix',
                                 lineColor = [-1,-1,-1],
                                 fillColor = [-1,-1,-1],
                                 pos = (0,0))
    fix_cross_horiz.draw() #This will draw the line onto the window
    fix_cross_vert.draw() #This will draw the line onto the window

# Create the line stimulus
def line(line_length): # Define the horizontal line where its lenght will change alongside the loop iteration number
    hor_line = visual.Rect(win0,
                       width = line_length,
                       height = 1,
                       units = 'pix',
                       lineColor = [-1,-1,-1],
                       fillColor = [-1,-1,-1],
                       pos = (0,0))
    hor_line.draw()

# Create the cross appearing after click
def cross(itspos):
    first_seg = visual.Rect(win0,
                            width = 9,
                            height = 1,
                            units = 'pix',
                            lineColor = [-1,-1,-1],
                            fillColor = [-1,-1,-1],
                            pos = itspos,
                            ori = 45)
    second_seg = visual.Rect(win0,
                             width = 9,
                             height = 1,
                             units = 'pix',
                             lineColor = [-1,-1,-1],
                             fillColor = [-1,-1,-1],
                             pos = itspos,
                             ori = 135)
    first_seg.draw()
    second_seg.draw()

# Create flankers for each condition
def flankers(string, pos):
    left = visual.TextStim(win0,
                            text = string[0],
                            pos = (pos[0],0),
                            color = (-1,-1,-1),
                            units = 'pix',
                            height = 22)

    right = visual.TextStim(win0,
                            text = string[1],
                            pos = (pos[1], 0),
                            color = (-1,-1,-1),
                            units = 'pix',
                            height = 22)
    left.draw()
    right.draw()

#Create the command for each trial
def command(text):
    command_string = visual.TextStim(win0,
                                    text = text,
                                    pos = (0,200),
                                    color = (-1,-1,-1),
                                    units = 'pix',
                                    height = 32,
                                    wrapWidth = 1920)
    command_string.draw()

# Wait for subjects to press enter (when they're ready)
text_info = visual.TextStim(win0,
                            text = 'PRESS ENTER TO START',
                            pos = (0,0),
                            color = (-1,-1,-1),
                            units = 'pix',
                            height = 32)
text_info.draw()
win0.flip()
key = event.waitKeys(maxWait = 9999, keyList = ('return', 'q'), clearEvents = True)

if 'return' in key:
    win0.flip()
    core.wait(1)
    pass # Go on in the code

if 'q' in key: # Exit whenever you want
    win0.close()
    core.quit()
    print('OK, program and window closed.')

# Update the subject on what task to do (training)
text_info_block = visual.TextStim(win0,
                               text = 'This is the Training Block',
                               pos = (0, 100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info = visual.TextStim(win0,
                         text = 'Pinpoint the following values',
                         pos = (0,0),
                         color = (-1,-1,-1),
                         units = 'pix',
                         height = 32)
text_info_start = visual.TextStim(win0,
                               text = 'Press Enter to Start',
                               pos = (0,-100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info_block.draw()
text_info.draw()
text_info_start.draw()
win0.flip()

keys = event.waitKeys(maxWait = 9999, keyList = ['return','q'], clearEvents = True)

if 'return' in key:
    win0.flip()
    core.wait(1)
    pass # Go on in the code

if 'q' in keys:
    win0.close()
    core.quit()

# Training loop
for i in range(0, 5):

    event.clearEvents()
    fixation_cross()
    win0.flip()
    core.wait(0.5)

    newxy = (sample(range(-300,300), 2)) # Generates random new coordinates for mouse every trial
    mymouse = event.Mouse(visible=True, newPos=((newxy[0]), (newxy[1])), win=win0) # New coordinates for the mouse

    stringpos = (-(conditions_random[i][0])/2-20, conditions_random[i][0]/2+20) # Set the position of flankers each trial

    if conditions_random[i][1] == 'nonum': # Set the text of flankers each trial in case of no number interval (empty)
        string = ('','')

    else:
        string = conditions_random[i][1] # Set the text of flankers each trial

    line(conditions_random[i][0]) # This time, these measures are taken from the pandas-to-numpy database
    command('PINPOINT THE VALUE: ' + conditions_random[i][2]) # Display the trial request
    flankers(string, stringpos)
    win0.flip()

    start_time = clock.getTime() # Starting our timer

    while True:

        buttons = mymouse.getPressed() # It means: "Execute while button is NOT pressed"

        quitkey = event.getKeys(keyList = ['q'])
        if 'q' in quitkey:
            win0.close()
            core.quit()

        elif buttons[0]:

            posmouse = (mymouse.getPos()) # ATTENTION: real coordinates of clicks are not considered
            posmouse = (posmouse[0], 0) # Cross coordinates normalized to (x, 0)
            line(conditions_random[i][0])
            flankers(string, stringpos)
            command('PINPOINT THE VALUE: ' + conditions_random[i][2])
            cross(posmouse)
            win0.flip()
            core.wait(0.5)
            break

# Update the subject on what task to do (test)
text_info_block = visual.TextStim(win0,
                               text = 'This is the Test Block',
                               pos = (0, 100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info = visual.TextStim(win0,
                         text = 'Pinpoint the following values',
                         pos = (0,0),
                         color = (-1,-1,-1),
                         units = 'pix',
                         height = 32)
text_info_start = visual.TextStim(win0,
                               text = 'Press Enter to Start',
                               pos = (0,-100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info_block.draw()
text_info.draw()
text_info_start.draw()
win0.flip()

keys = event.waitKeys(maxWait = 9999, keyList = ['return','q'], clearEvents = True)

if 'return' in key:
    win0.flip()
    core.wait(1)
    pass # Go on in the code

if 'q' in keys:
    win0.close()
    core.quit()

# Main loop
for i in range(0, len(line_length_array)):

    trial_no_array.append(i)
    sub_id_array.append(show_dlg[1])
    date_value_array.append(date_val)
    time_value_array.append(datetime.now().strftime('%H%M%S'))
    final_line_length_array.append(conditions_random[i][0])
    final_numbers_interval_array.append(conditions_random[i][1])
    final_number_requested_array.append(conditions_random[i][2])
    final_real_value_array.append(conditions_random[i][3])

    event.clearEvents()
    fixation_cross()
    win0.flip()
    core.wait(0.8)

    newxy = (sample(range(-300,300), 2))
    mymouse = event.Mouse(visible=True, newPos=((newxy[0]), (newxy[1])), win=win0)

    stringpos = (-(conditions_random[i][0])/2-20, conditions_random[i][0]/2+20)

    if conditions_random[i][1] == 'nonum':
        string = ('','')

    else:
        string = conditions_random[i][1]

    command('PINPOINT THE VALUE: ' + conditions_random[i][2])
    line(conditions_random[i][0]) # This time, these measures are taken from the pandas-to-numpy database
    flankers(string, stringpos)
    win0.flip()

    start_time = clock.getTime() # Starting our timer
    while True:

        buttons = mymouse.getPressed()

        quitkey = event.getKeys(keyList = ['q'])
        if 'q' in quitkey:
            win0.close()
            core.quit()

        elif buttons[0]:

            stop_timer = clock.getTime()
            delta_time = ('%.4f' %((stop_timer - start_time)*1000)) # Rounded to four digits. Converted in milliseconds

            posmouse = (mymouse.getPos()) # ATTENTION: real coordinates of clicks are not considered
            posmouse = (posmouse[0], 0)
            line(conditions_random[i][0])
            flankers(string, stringpos)
            command('PINPOINT THE VALUE: ' + conditions_random[i][2])
            cross(posmouse)
            win0.flip()
            core.wait(0.5)
            break

    click_pos.append(posmouse) # Cross coordinates are saved
    response_latency.append(delta_time)

# Create our output table in pandas
output_file = pd.DataFrame({'Trial_No':trial_no_array,
                            'SubID':sub_id_array,
                            'Date':date_value_array,
                            'Time':time_value_array,
                            'Line_Length':final_line_length_array,
                            'Numbers intervals': final_numbers_interval_array,
                            'Request': final_number_requested_array,
                            'Sub_response':click_pos,
                            'Latency_ms':response_latency,
                            'Real Value': final_real_value_array})

output_file.to_csv(save_file_name, sep = ',', index = False) # Saving it as .csv in the path declared at the start.

win0.close()
print('OK, program and window closed.')
