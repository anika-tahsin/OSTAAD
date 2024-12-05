import add_contacts
import view_contacts
import delete_contact
import search_contact

#all_contacts = []
all_contacts = view_contacts.view_contacts()
#print(all_contacts)

while True:
    print("Welcome to Contact Book ")
    print("0. Exit")
    print("1. View all contacts")
    print("2. Add Contact")
    print("3. Delete contact")
    print("4. Search contact")

    option = input("Please choose your option from the above list: ")

    if option == '0':
        print("Thanks for using Contact Book")
        break
    elif option == '1':
        contacts = view_contacts.display_contacts(all_contacts)
        
    elif option == '2':
        print("Add contact: ")
        contacts = add_contacts.add_contact(all_contacts)
        print(all_contacts)

    elif option == '3':
        print("Delete contact")
        contacts = delete_contact.delete_contact()
        
    
    elif option == '4':
        print("\nSearch contact: ")
        contact = search_contact.search_contact()
       
            
    else:
        print("Please choose options from 0 to 3 only")
