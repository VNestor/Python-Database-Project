from tkinter import *
import tkinter as tk
from tkinter import messagebox


def onselect(evt):
    global selected_index
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selected_index = index
    display_note(index, value)


def display_note(index, value):
    global note_ids, conn
    # Cleear the fields
    note_title.delete(0, tk. END)
    note_text.delete('1.0', tk.END)

    data = db_select_specific_note(conn, notes_ids[index])

    # Insert data
    note_title.insert(tk.END, data[0])
    note_text.insert(tk.END, data[1])

    # Enable delete and edit button
    btn_delete.config(state=tk.NORMAL)
    btn_edit.config(state=tk.NORMAL)
