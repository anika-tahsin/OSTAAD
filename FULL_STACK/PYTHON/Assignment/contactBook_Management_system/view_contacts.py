
def view_contacts(contacts):
    
    
    if contacts != []:
        for contact in contacts:
            print(f"Name: {contact['name']}\n Phone No: {contact['phone_no']}\n Email ID: {contact['email']}\n Address: {contact['address']}\n")

    else:
        print("No contacts in the contact book")