
import csv, os
import save_contacts

def delete_contact():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "contacts.csv" )

    if not os.path.exists(file_path):
        print("No contacts found. The file does not exist.")
        return 
    
    contact_to_delete = input("Enter the phone number you want to search: ").strip()
    contacts = []
    found = False
    
    try:
        with open (file_path, "r", newline='') as myFile:
            contactReader = csv.DictReader(myFile)
            for contact in contactReader:
                if contact_to_delete == contact['phone_no']:
                    found = True
                    print(f"Deleting Contact: Name: {contact['name']},Phone No: {contact['phone_no']}, Email: {contact['email']}, Address: {contact['address']}")
                else:
                    contacts.append(contact)
                
                      
    except Exception as e:
        print(f"Error reading contacts- {e}")
        return

    if found:
        try:
            save_contacts.save_contacts(contacts)
            print("Contact deleted successfully")
        except Exception as e:
            print(f"Error saving updated contact- {e}")
    else:
        print("No matching contacts found")


