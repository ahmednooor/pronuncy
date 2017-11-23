"""
    PRONUNCY - English Pronunciation App
    Author: Ahmed Noor
"""

# --- imports
import os
import sys
from tkinter import (
    Tk,
    StringVar,
    Scrollbar,
    Listbox,
    Menu,
    VERTICAL,
    END,
    N,
    S,
    E,
    W,
    font,
    messagebox,
    ttk
)
# import pyglet
import pygame as pg


"""
    Preps
"""

# --- configure root directory path relative to this file
THIS_FOLDER_G = ""

if getattr(sys, "frozen", False):
    # frozen
    THIS_FOLDER_G = os.path.dirname(sys.executable)
else:
    # unfrozen
    THIS_FOLDER_G = os.path.dirname(os.path.realpath(__file__))


# --- load "avbin" lib to pyglet
# pyglet.lib.load_library(THIS_FOLDER_G + "/assets/lib/avbin.dll")
# pyglet.have_avbin = True


# --- init sound variable for later use
# sound_obj = pyglet.media.load(THIS_FOLDER_G + "/assets/media/pyglet_init.mp3")
# sound_obj.play()
sound_obj = None


# --- list to store words
words_list = []

# --- generate and load list of words from the list of audio files into words_list
def populateWordList():
    global words_list

    words_list = os.listdir(THIS_FOLDER_G + "/assets/eng-wcp-us")
    words_list_LEN = len(words_list)

    for i in range(words_list_LEN):
        words_list[i] = words_list[i][6:-4]

    words_list = sorted(words_list, key=str.lower)

populateWordList()


"""
    Frontend Creation
"""

# --- init tkinter
root = Tk()
root.title("PRONUNCY")
root.iconbitmap(THIS_FOLDER_G + "/assets/media/favicon.ico")


# --- show about info
def show_about_info():
    messagebox.showinfo("About",
                        """PRONUNCY is an English Pronunciation App
Author: Ahmed Noor
Credits: Pronunciations from Wikimedia Commons (CC 2.0)
Made With: Python3.6 , Tkinter & Pyglet || Pygame""")


# --- create menu bar and options
menu_bar = Menu(root)
menu_bar.add_command(label="About",
                     command=show_about_info)
menu_bar.add_command(label="Quit!",
                     command=root.quit)

# --- add menu bar to root window
root.config(menu=menu_bar)

# --- config default font in tkinter
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=11)
root.option_add("*Font",
                default_font)


# --- add Frame to hold search bar & label
search_frame = ttk.Frame(root,
                         padding="16 10 16 10")
search_frame.grid(column=0,
                  row=0,
                  sticky=(N, W, E, S))
search_frame.columnconfigure(0,
                             weight=1)
search_frame.rowconfigure(0,
                          weight=1)


# --- add search label
search_label = ttk.Label(search_frame,
                         width=40,
                         text="Search Word",
                         padding="0 0 0 6")
search_label.grid(column=0,
                  row=0,
                  sticky=(W, E))


# --- tkinter specific variable to store input from search bar
search_query = StringVar()


# --- add search bar
search_bar = ttk.Entry(search_frame,
                       width=40,
                       textvariable=search_query)
search_bar.grid(column=0,
                row=2,
                sticky=(W, E))


# --- add Frame to hold listbox bar & label
list_frame = ttk.Frame(root,
                       padding="16 10 16 18")
list_frame.grid(column=0,
                row=1,
                sticky=(N, W, E, S))
list_frame.columnconfigure(0,
                           weight=1)
list_frame.rowconfigure(0,
                        weight=1)


# --- add listbox label
words_list_label = ttk.Label(list_frame,
                             width=40,
                             text="Double Click to Play or Select and Press Enter",
                             padding="0 0 0 6")
words_list_label.grid(column=0,
                      row=0,
                      sticky=(W, E))


# --- add scroll bar for listbox
scroll_bar = Scrollbar(list_frame,
                       orient=VERTICAL)
scroll_bar.grid(column=1,
                row=1,
                sticky=(N, W, E, S))


# --- add listbox
words_list_box = Listbox(list_frame,
                         width=40,
                         height=14,
                         yscrollcommand=scroll_bar.set)
words_list_box.grid(column=0,
                    row=1,
                    sticky=(N, W, E, S))


# --- populate the listbox with words from words_list
def populate_list_box():
    global words_list_box, words_list

    for index, word in enumerate(words_list):
        words_list_box.insert(index, word)

populate_list_box()


# --- config scroll_bar to move according to the listbox
scroll_bar.config(command=words_list_box.yview)


"""
    Backend Functions
"""



def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    # clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except:
        print("File {} not found!".format(music_file))
        return
    pg.mixer.music.play()
    # while pg.mixer.music.get_busy():
    #     # check if playback has finished
    #     clock.tick(30)


# --- play audio file
def play_audio_file(evt):
    global sound_obj

    evt_widget = evt.widget
    index = int(evt_widget.curselection()[0])
    value = evt_widget.get(index)

    play_music(THIS_FOLDER_G + "/assets/eng-wcp-us/En-us-" + value + ".mp3")
    # sound_obj = pyglet.media.load(THIS_FOLDER_G + "/assets/eng-wcp-us/En-us-" + value + ".mp3")
    # sound_obj.play()
    # sound_obj = None


# --- decorator for binding functions to tkinter widgets
def bind(widget, event):
    def decorator(func):
        widget.bind(event, func)

        return func

    return decorator


# --- bind mouse double click to listbox items and play respective files
@bind(words_list_box, "<Double-Button-1>")
def on_dbl_click(evt):
    return play_audio_file(evt)


# --- bind return/enter key to listbox items and play respective files
@bind(words_list_box, "<Return>")
def on_return_key_press(evt):
    return play_audio_file(evt)


# --- clear highlighting selection of previous input upon focusing in the search bar
@bind(search_bar, "<FocusIn>")
def on_focus_in(evt):
    evt.widget.selection_clear()


# --- function to update listbox according to the input in search bar
def update_list_box(*args):
    global search_query, words_list_box, words_list

    query = search_query.get()

    populateWordList()
    words_list_box.delete(0, END)

    if query and query.strip(" \t\r\n") != "":
        words_list = filter(lambda word:
                            query.lower().replace(" ", "_") in word.lower() != -1 or
                            query.lower().replace(" ", "-") in word.lower() != -1,
                            words_list)

    populate_list_box()


# --- trace input in search bar via the search_query variable and update listbox
search_query.trace("w", update_list_box)


# --- run app
if __name__ == "__main__":
    root.mainloop()
