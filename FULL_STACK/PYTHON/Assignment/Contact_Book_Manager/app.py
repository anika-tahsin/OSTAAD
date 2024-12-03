from view_contacts import view_contacts, display_contacts
from save_contacts import save_contacts
from add_contacts import add_contact, is_duplicate,get_contact
import search_contacts
import delete_contacts

filename = "contacts.csv"


def main():

    contacts = view_contacts(filename)
    while True:
        print("Welcome to Contact Book ")
        print("0. Exit")
        print("1. View all contacts")
        print("2. Add Contact")
        print("3. Delete contact")
        print("4. Search contact")

        option = input("Please choose your option from the above list: ").strip()

        if option == '0':
            print("Thanks for using Contact Book")
            break
        elif option == '1':
            print("View all your contacts")
            display_contacts(contacts)
            
        elif option == '2':
            print("Add contact: ")
            get_contact()
            if is_duplicate == True:
                print("\n The contact is already in the book")
                continue
            

        elif option == '3':
            contacts = delete_contacts(contacts)
            print("Deleted contact")
        
        elif option == '4':
            contacts = search_contacts.search_contact(all_contacts)
            print("The contact you are looking for is:\n")
        else:
            print("Please choose options from 0 to 3 only")


main()