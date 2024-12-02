import add_contacts
import view_contacts
import delete_contact
import search_contact

all_contacts = []

while True:
    print("Welcome to Contact Book ")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View all contacts")
    print("3. Delete contact")
    print("4. Search contact")

    option = input("Please choose your option from the above list: ")

    if option == '0':
        print("Thanks for using Contact Book")
        break
    elif option == '1':
        print("Add contact: ")
        contacts = add_contacts.add_contact(all_contacts)
        print(contacts)
    elif option == '2':
        print("View all your contacts")
        contacts = view_contacts.view_contacts(all_contacts)

    elif option == '3':
        contacts = delete_contact.delete_contact(all_contacts)
        print("Deleted contact")
    
    elif option == '4':
        contacts = search_contact.search_contact(all_contacts)
        print("The contact you are looking for is:\n")
    else:
        print("Please choose options from 0 to 3 only")
