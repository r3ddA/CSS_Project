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

def add_contact(name, phone):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()

def delete_contact(name):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
    conn.commit()
    conn.close()

def search_contact(name):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts WHERE name = ?', (name,))
    contact = cursor.fetchone()
    conn.close()
    if contact:
        print(f"Found contact: Name: {contact[1]}, Phone: {contact[2]}")
    else:
        print("Contact not found.")

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