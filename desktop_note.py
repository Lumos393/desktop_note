import os
import sys
import tkinter as tk
import datetime as dt
import xml

uinput = input("Enter note now \n ")
print("e1")

notes = open("notes.xml", "a")
print("e2")
notes.write(uinput)
print("e3")

print(notes.read)