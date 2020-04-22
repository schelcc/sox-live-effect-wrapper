#!/bin/python3

from tkinter import *
import os, threading
from tkinter import ttk

os.system("pactl load-module module-null-sink")
os.system("pacmd set-default-source null.monitor")
os.environ["LADSPA_PATH"] = "$LADSPA_PATH:/usr/lib/ladspa"

window = Tk()

window.title("Mic FX app")
window.geometry('500x160')

cur_arg = 'sox -t pulseaudio default -t pulseaudio null '

reverb_bool = False
pitch_bool = False
autotune_bool = False


pitch_slider = Scale(window, from_=-800, to=800, orient=HORIZONTAL)
reverb_slider = Scale(window, from_=0, to=100, orient=HORIZONTAL)

def close():
    os.system("killall sox")
    os.system("pactl unload-module module-null-sink")
    exit()

def reverb():
    global reverb_bool
    reverb_bool = True

    msg = "Reverb: " + str(reverb_slider.get())
    reverb_title.configure(text=msg)

def pitch():
    global pitch_bool
    pitch_bool = True
    print(pitch_bool)

    msg = "Pitch: " + str(pitch_slider.get())
    pitch_title.configure(text=msg)

def autotune():
    global autotune_bool
    autotune_bool = True

    msg = "Autotune: on"
    autotune_title.configure(text=msg)

def clean():
    global reverb_bool
    global pitch_bool

    global cur_arg

    cur_arg = 'sox -t pulseaudio default -t pulseaudio null '

    reverb_title.configure(text="")
    pitch_title.configure(text="")

    reverb_bool = False
    pitch_bool = False
    autotune_bool = False

    def callback():
        os.system("killall sox")
        os.system(cur_arg)
    t = threading.Thread(target=callback)
    t.start()

    print("cleaned")

def add_effects():
    global reverb_bool
    global pitch_bool

    global cur_arg

    if reverb_bool:
        cur_arg += "reverb " + str(reverb_slider.get()) + " "
        print("added rev")
    if pitch_bool:
        cur_arg += "pitch " + str(pitch_slider.get()) + " "
        print("added pitch")
    if autotune_bool:
        cur_arg += "ladspa -r autotalent 440 69 0 0 5 0 0 -1.1 0 -1.1 0 0 -55 0 -1.1 1 0 0 0 0 5 0 0 0 0 0 1 0 0 0"
        print("added autotune")
    
    def callback():
        os.system("killall sox")
        os.system(cur_arg)
    t = threading.Thread(target=callback)
    t.start()

    print(cur_arg)

def get_vars():
    global reverb_bool
    global pitch_bool

def quit():
    os.system("killall sox")
    exit()

menu = Menu(window)

file_menu = Menu(menu)
file_menu.add_command(label="Quit", command=quit)

menu.add_cascade(label='File', menu=file_menu)

reverb_toggle = Button(window, text="Reverb", command=reverb)
pitch_toggle = Button(window, text="Pitch", command=pitch)
autotune_toggle = Button(window, text="Autotune", comman=autotune)
add_all = Button(window, text="Add effects", command=add_effects)
clean_stream = Button(window, text="Clear all effects", command=clean)
exit_button = Button(window, text="Exit", command=close)

effects_title = Label(window, text="Effects to add")
reverb_title = Label(window, text="")
pitch_title = Label(window, text="")
autotune_title = Label(window, text="")

reverb_toggle.grid(column=0, row=0)
pitch_toggle.grid(column=1, row=0)
autotune_toggle.grid(column=2, row=0)
clean_stream.grid(column=3, row=0)
add_all.grid(column=3, row=1)
pitch_slider.grid(column=1, row=1)
reverb_slider.grid(column=0, row=1)
exit_button.grid(column=3, row=3)
effects_title.grid(column=0, row=3)
reverb_title.grid(column=0, row=4)
pitch_title.grid(column=0, row=5)
autotune_title.grid(column=0, row=6)

window.config(menu=menu)

print(cur_arg)

window.mainloop()