import os
import sys
import tkinter as tk
import datetime as dt
import xml

uinput = input("Enter note now\n")
#set up input
notes = open("notes.xml", "a")
#open notes.xml file

notes.write(uinput + "\n\n")
#call input and write to notes

notes.close
#close notes