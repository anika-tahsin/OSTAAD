import add_contacts
import view_contacts

contacts = []

while True:
    print("Welcome to Contact Book ")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View all contacts")
    print("3. Delete contact")

    option = input("Please choose your option from the above list: ")

    if option == '0':
        print("Thanks for using Contact Book")
        break
    elif option == '1':
        print("Add contact: ")
        contacts = add_contacts.add_contact(contacts)
    elif option == '2':
        print("View all your contacts")
        contacts = view_contacts.view_contacts(contacts)

    elif option == '3':
        print("Delete a contact")
    else:
        print("Please choose options from 0 to 3 only")
