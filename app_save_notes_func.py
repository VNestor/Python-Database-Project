def save_note():
    global conn
    title - note_title.get()

    if len(title) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter the note title")
        return

    note = note_text.get("1.0", tk.END)
    if len(note.rstrip()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter the notes")
        return

    # Check if title exist
    title_exist = False
    existing_titles = list_notes.get(0, tk.END)

    for t in existing_titles:
        if t == title:
            title_exist = True
            break

    if title_exist is True:
        tk.messagebox.showerror(
            title="ERROR!!!", message="Note title already exist, please choose a different title")
        return

    # Save in database
    inserted_id = db_insert_note(conn, title, note)
    print("Last inserted id is: " + str(inserted_id))

    # Insert into the listbox
    list_notes.insert(tk.END, title)
    # Save note id
    notes_ids.append(inserted_id)

    # Clear UI
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)
