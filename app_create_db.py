# Building a note taking app with an MySQL Backend
# This project was based upon the follwo9ng tutorial: https://levelup.gitconnected.com/build-a-note-taking-app-with-mysql-backend-in-python-927b4c5fad91

# This project is to help learn how to create a note takin app in python, while also learning tools, principles and concepts that can be applied to buildinf other applications

# Victor Nestor
# March 17, 2021

# This application will allow users to add a new note, view note details, edits, and delete existing notes
# The application relies on mysql database to store note data
# Begin with app backend: setting up and performing basic database CRUD operations then implement front end


import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306, user="root", passwd="")


def db_create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")


# Call the function
db_create_db(conn)
