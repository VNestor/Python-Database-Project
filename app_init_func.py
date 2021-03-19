from app_create_db import db_create_db, conn
from app_create_table import db_create_table
from app_select_query import db_select_all_notes
import tkinter as tk


def init(conn):
    # Create databse if it does not exist
    db_create_db(conn)
    # Create table if it does not exist
    db_create_table(conn)

    # Select data
    notes = db_select_all_notes(conn)

    for note in notes:
        list_notes.insert(tk.END, note[1])
        # Save the ID
        note_ids.append(note[0])


init(conn)
