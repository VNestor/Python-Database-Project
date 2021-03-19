from app_create_db import db_create_db
from app_create_db import conn


def db_create_table(conn):
    db_create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS tb_notes (" \
        "note_id INT AUTO_INCREMENT PRIMARY KEY, " \
            "title VARCHAR(225) NOT NULL, " \
        "note VARCHAR(2000) NOT NULL)"
    mycursor.execute(query)


# Call the function
db_create_table(conn)
