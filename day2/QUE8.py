import uuid

phonebook = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact_id = str(uuid.uuid4())
    phonebook[contact_id] = {
        "name": name,
        "phone": phone
    }

    print("Contact added successfully.")

def find_contacts_by_name(name):
    matches = []
    for cid, details in phonebook.items():
        if details["name"].lower() == name.lower():
            matches.append((cid, details))
    return matches

def display_matches(matches):
    for i, (cid, details) in enumerate(matches, start=1):
        print(f"{i}. {details['name']} - {details['phone']}")

def remove_contact():
    name = input("Enter name to remove: ")
    matches = find_contacts_by_name(name)

    if not matches:
        print("No contact found.")
        return

    display_matches(matches)
    choice = int(input("Select number to remove: ")) - 1

    if 0 <= choice < len(matches):
        del phonebook[matches[choice][0]]
        print("Contact removed.")
    else:
        print("Invalid choice.")

def update_contact():
    name = input("Enter name to update: ")
    matches = find_contacts_by_name(name)

    if not matches:
        print("No contact found.")
        return

    display_matches(matches)
    choice = int(input("Select number to update: ")) - 1

    if 0 <= choice < len(matches):
        new_phone = input("Enter new phone number: ")
        phonebook[matches[choice][0]]["phone"] = new_phone
        print("Contact updated.")
    else:
        print("Invalid choice.")

def search_contact():
    name = input("Enter name to search: ")
    matches = find_contacts_by_name(name)

    if not matches:
        print("No contact found.")
    else:
        display_matches(matches)

def show_all_contacts():
    if not phonebook:
        print("Phonebook is empty.")
        return

    print("\n--- All Contacts ---")
    for details in phonebook.values():
        print(f"{details['name']} - {details['phone']}")

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")
