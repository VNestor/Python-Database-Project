from app_create_db import conn


def db_insert_note(conn, title, note):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO tb_notes (title, note) VALUES (%s, %s)"
    val = (title, note)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid


records = [
    ('My first title', 'This is my first awesome note'),
    ('My second title', 'This is my second awesome note'),
    ('My third title', 'This is my third awesome note'),
    ('My fourth title', 'This is my fourth awesome note'),
    ('My fifth title', 'This is my fifth awesome note')
]

for v in records:
    # Call function
    db_insert_note(conn, v[0], v[1])
