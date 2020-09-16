#!/usr/bin/python3

### Pystab created by Joe Burgess.
### Must use python3 to run.


# libraries some are not used yet.
import subprocess
import time
import sys
import os
from os import listdir
from os.path import isfile, join
from tkinter import *

#######################################################################
### Required: Set the path to your log file here.
LOGFILE = "/home/homeDir/.wine/drive_c/Program Files (x86)/Sony/EverQuest/Logs/eqlog_charName_project1999.txt"
#######################################################################


############## DO NOT CHANGE THE CODE BELOW #################
################################################################

### Sets the label in tkinter
SPELL_NAME = "Back Stab Damage"
### Sets text to search for in log file
SPELL_TEXT = "You backstab"

### Opens the log file and moves to the last line ###
f = open(LOGFILE, 'r')
f.seek(0,2)
print("Reading Log File")

root=Tk()

### Funcion to Loop over log file and search for backstab ###
def read_log():
    line = f.readline()
    if SPELL_TEXT in line:
        l2["text"] =  line   
        root.after(50, read_log)
    else:
        root.after(50, read_log)

### Closes the log file and exits program ###
def exit_prog():
    f.close()
    root.quit()              
    print("Closing log file and exiting")

### Widgets and layout for GUI ###
root.geometry("700x100")
root.title("Pystab")
l1=Label(root,font="times 18",text=SPELL_NAME)
l1.pack()
l2=Label(root, font="times 15", text = "")
l2.pack()
btn1=Button(root, text="Exit", command = exit_prog)
btn1.pack()

### Starts the program.###
root.after(50, read_log)

root.mainloop()

