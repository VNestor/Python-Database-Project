def delete_note():
    global selected_index, conn, notes_ids
    title = note_title.get()
    notes = note_text.get("1.0", tk.END)

    print("Selected note is: " + str(selected_index))

    if len(title) < 1 or len(notes.rstrip()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!!", message="Please select a note to delete")
        return

    result = tk.messagebox.askquestion(
        "Delete", "Are you sure you want to delete this note?", icon='warning')

    if result == 'yes':
        # Remove notes from database
        note_id = notes_ids[selected_index]
        db_delete_note(conn, note_id)
        del notes_ids[selected_index]

        # Remove from UI
        note_title.delete(0, tk.END)
        note_text.delete('1.0', tk.END)
        list_notes.delete(selected_index)
