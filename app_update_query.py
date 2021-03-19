from app_create_db import conn


def db_update_note(conn, title, note, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE tb_notes SET title = %s, note = %s WHERE note_id = %s"
    val = (title, note, note_id)
    mycursor.execute(query, val)
    conn.commit()


# Call the function
db_update_note(conn, "My fifth title - updated",
               "this is my fifth awesome note - updated", "5")
