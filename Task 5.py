import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create the contacts table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        email TEXT,
        address TEXT
    )
''')
conn.commit()

def add_contact():
    """Add a new contact."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email (optional): ").strip()
    address = input("Enter Address (optional): ").strip()

    try:
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                       (name, phone, email, address))
        conn.commit()
        print("Contact added successfully!")
    except sqlite3.IntegrityError:
        print("Error: A contact with this phone number already exists.")

def view_contacts():
    """Display all contacts."""
    cursor.execute("SELECT id, name, phone FROM contacts")
    contacts = cursor.fetchall()

    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"{contact[0]}. {contact[1]} - {contact[2]}")

def search_contact():
    """Search contacts by name or phone number."""
    query = input("Enter Name or Phone Number to search: ").strip()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()

    if not results:
        print("No matching contacts found.")
    else:
        print("\nSearch Results:")
        for contact in results:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")

def update_contact():
    """Update an existing contact."""
    view_contacts()
    contact_id = input("\nEnter Contact ID to update: ").strip()

    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()

    if contact:
        new_name = input(f"Enter new name ({contact[1]}): ").strip() or contact[1]
        new_phone = input(f"Enter new phone ({contact[2]}): ").strip() or contact[2]
        new_email = input(f"Enter new email ({contact[3]}): ").strip() or contact[3]
        new_address = input(f"Enter new address ({contact[4]}): ").strip() or contact[4]

        try:
            cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?",
                           (new_name, new_phone, new_email, new_address, contact_id))
            conn.commit()
            print("Contact updated successfully!")
        except sqlite3.IntegrityError:
            print("Error: Phone number must be unique.")
    else:
        print("Contact not found.")

def delete_contact():
    """Delete a contact."""
    view_contacts()
    contact_id = input("\nEnter Contact ID to delete: ").strip()

    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()

    if cursor.rowcount:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    """Main menu for the Contact Management System."""
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

    conn.close()

# Run the application
if __name__ == "__main__":
    main()
