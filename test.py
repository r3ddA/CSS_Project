from app import ContactsApp

def test_add_contact():
    app = ContactsApp()
    app.add_contact("John Doe", "1234567890")
    app.add_contact("Jane Smith", "0987654321")
    app.add_contact("Alice Johnson", "5555555555")
    app.add_contact("Bob Brown", "4444444444")
    contacts = app.get_contacts()
    assert len(contacts) == 4
    assert "John Doe" in contacts
    assert "Jane Smith" in contacts
    assert "Alice Johnson" in contacts
    assert "Bob Brown" in contacts
    print("test_add_contact passed")

def test_delete_contact(app):
    app.delete_contact("John Doe")
    contacts = app.get_contacts()
    assert len(contacts) == 3
    assert "John Doe" not in contacts
    assert "Jane Smith" in contacts
    assert "Alice Johnson" in contacts
    assert "Bob Brown" in contacts
    print("test_delete_contact passed")

def test_search_contact(app):
    contact = app.search_contact("Jane Smith")
    assert contact is not None
    assert contact['name'] == "Jane Smith"
    assert contact['phone'] == "0987654321"
    print("test_search_contact passed")

def test_show_contacts(app):
    contacts = app.get_contacts()
    assert len(contacts) == 3
    assert "Jane Smith" in contacts
    assert "Alice Johnson" in contacts
    assert "Bob Brown" in contacts
    print("test_show_contacts passed")

if __name__ == "__main__":
    app = ContactsApp()
    test_add_contact()
    test_show_contacts(app)
    test_delete_contact(app)
    test_show_contacts(app)
    test_search_contact(app)
    print("All tests passed!")