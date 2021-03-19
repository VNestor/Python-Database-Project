from app_create_db import conn


def db_select_all_notes(conn):
    conn.database = "db_notes"
    query = "SELECT * from tb_notes"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_select_specific_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute(
        "SELECT title, note FROM tb_notes WHERE note_id = " + str(note_id))
    return mycursor.fetchone()


# Call the functions
print("----------------Selecting all records-------------")
# Select all notes
data = db_select_all_notes(conn)
for d in data:
    print(d)

print("--------Selecting record where note_id is 2-------")
print(db_select_specific_note(conn, 2))
