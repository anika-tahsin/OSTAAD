import os
from view_contacts import view_contacts
from save_contacts import save_contacts
from add_contacts import add_contact, is_duplicate
import search_contacts
import delete_contacts

# Specify the CSV file name
filename = "contacts.csv"

def display_contacts(contacts):
    """
    Display all contacts in a formatted way.
    """
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nContacts:")
    print("-" * 40)
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
    print("-" * 40)

def main():
    # Load contacts from the CSV file
    contacts = view_contacts(filename)

    while True:
        print("\nContact Book")
        print("1. View Contacts")
        print("2. Add New Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            # View all contacts
            display_contacts(contacts)

        elif choice == "2":
            # Add a new contact
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()

            # Check for duplicate phone number
            if is_duplicate(contacts, phone):
                print("\nA contact with this phone number already exists!")
                continue

            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()

            new_contact = [name, phone, email, address]
            contacts.append(new_contact)
            add_contact(filename, new_contact)
            print("\nContact added successfully!")

        elif choice == "3":
            # Search for a contact
            phone = input("Enter Phone Number to Search: ").strip()
            contact = search_contacts(contacts, phone)
            if contact:
                print("\nContact Found:")
                print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
            else:
                print("\nNo contact found with that phone number.")

        elif choice == "4":
            # Delete a contact
            phone = input("Enter Phone Number to Delete: ").strip()
            delete_contacts(filename, contacts, phone)

        elif choice == "5":
            print("\nExiting the Contact Book. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()