import sys
from utils import add_contact, delete_contact, search_contact, list_contacts, initialize_db

def main():
    initialize_db()
    
    while True:
        print("\nContacts App")
        print("1. See all contacts")
        print("2. Add a contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            list_contacts()
        elif choice == '2':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '4':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()