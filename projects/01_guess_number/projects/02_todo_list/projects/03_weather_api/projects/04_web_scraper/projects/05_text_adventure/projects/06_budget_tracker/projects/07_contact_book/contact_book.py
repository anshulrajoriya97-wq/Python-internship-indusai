contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"✅ Contact added: {name} - {phone}")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("📒 Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"❌ Contact deleted: {name}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
