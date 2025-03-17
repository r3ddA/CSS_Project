import sqlite3

def initialize_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def delete_contact(name):
   hfvbuhjgfb egbue tuvkn


def mango():
    print("Mango")
    
def list_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    if contacts:
        for contact in contacts:
            print(f"Name: {contact[1]}, Phone: {contact[2]}")
    else:
        print("No contacts found.")