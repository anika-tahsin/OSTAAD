
import csv, os


def view_contacts():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "contacts.csv" )

    if not os.path.exists(file_path):
        print("No contacts found. The file does not exist.")
        return []
    
    contacts = []
    
    try:
        with open (file_path, "r", newline='') as myFile:
            contactReader = csv.DictReader(myFile)
            print("Contacts")
            for contact in contactReader:
                print(f"Name: {contact['name']},Phone No: {contact['phone_no']}, Email: {contact['email']}, Address: {contact['address']}")
                contacts.append(contact)
                      
    except Exception as e:
        print(f"Error reading contacts- {e}")

    return contacts


def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!")

    else:
        print("\nAll contacts: ")
        print('-'*50)
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']},Phone No: {contact['phone_no']}, Email: {contact['email']}, Address: {contact['address']}")
        print('-'*50)