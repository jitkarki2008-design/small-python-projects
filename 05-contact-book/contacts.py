# Project 05 - Contact Book with JSON
import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f) # loads dict from file
    except FileNotFoundError:
        return {} # empty dict = no contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4) # save dict nicely

contacts = load_contacts()

print("--- Your Contact Book ---")

while True:
    print("\n1. View 2. Add 3. Search 4. Delete 5. Exit")
    choice = input("Choose (1-5): ")

    if choice == '1':
        if not contacts:
            print("No contacts yet!")
        else:
            print("\nYour Contacts:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == '2':
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        contacts[name] = phone # dict syntax: contacts[key] = value
        save_contacts(contacts)
        print(f"Saved {name}")

    elif choice == '3':
        search = input("Enter name to search: ").strip()
        if search in contacts:
            print(f"{search} : {contacts[search]}")
        else:
            print("Not found!")

    elif choice == '4':
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            removed = contacts.pop(name)
            save_contacts(contacts)
            print(f"Deleted {name}")
        else:
            print("Not found!")

    elif choice == '5':
        print("Bye! Saved in contacts.json")
        break
    else:
        print("Invalid choice")