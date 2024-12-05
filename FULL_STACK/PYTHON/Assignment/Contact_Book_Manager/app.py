from view_contacts import view_contacts, display_contacts
from save_contacts import save_contacts
from add_contacts import add_contacts, is_duplicate
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
            print("\nThanks for using Contact Book")
            break
        elif option == '1':
            print("\nView all your contacts")
            display_contacts(contacts)
            
        elif option == '2':
            print("\nAdd contact: ")
            name = input("Name of the Contact person: ").strip()
            if name.isalpha() == True:
                pass
            else:
                print("Please enter name in words")
                name = input("Name of the Contact person: ").strip()
            
            phone_no = (input("Phone no of the Contact person: ")).strip()
            try:
                int_phone_no = int(phone_no)
                     
            except ValueError:
                print("Please enter digits only for phone number")
                phone_no = int(input("Phone no of the Contact person: "))
                

            email = input("Email ID of the Contact person: ").strip()
            try: 
                email.index("@")
                str(email)
                pass
            except Exception as e:
                print("Enter correct email format")
                email = input("Email ID of the Contact person: ").strip()

            address = input("Address of the Contact person: ").strip()

            new_contact = [name, phone_no, email, address]
            contacts.append(new_contact)
            add_contacts(filename, new_contact)
            
            if is_duplicate == True:
                print("\n The contact is already in the book")
                continue 
        else:
            print("Please choose options from 0 to 3 only")
        """   
        elif option == '3':
            contacts = delete_contacts(contacts)
            print("Deleted contact") """
        """ 
        elif option == '4':
            contacts = search_contacts.search_contact(all_contacts)
            print("The contact you are looking for is:\n") 
        """
        


main()