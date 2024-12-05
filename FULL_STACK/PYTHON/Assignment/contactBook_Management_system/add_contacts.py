
from save_contacts import save_contacts

def add_contact(all_contacts):
    
    while True:
        name = input("Name of the Contact person: ").strip()
        if name.replace(" ", "").isalpha():
            break
        
        print("Please enter only alphabatic characters.")
        name = input("Name of the Contact person: ")

    while True:

        try:
            phone_no = input("Phone no of the Contact person: ").strip()
            if not phone_no.isdigit() or len(phone_no)< 11:
                raise ValueError("Phone number must contain only digits and have at least 11 digits. ")
            if any(contact['phone_no'] == int(phone_no) for contact in all_contacts):
                print("This phone number already exists. Try again.")
            else:
                phone_no = int(phone_no)
                break

        except ValueError as e:
            print(e)
            
    
    email = input("Email ID of the Contact person: ")
    try: 
        email.index("@")
        str(email)
        pass
    except Exception as e:
        print("Enter correct email format")
        email = input("Email ID of the Contact person: ")

    address = input("Address of the Contact person: ").strip()

    contacts ={
        "name":name,
        "phone_no":phone_no,
        "email":email,
        "address": address
    }

    all_contacts.append(contacts)
    save_contacts(all_contacts)

    print("Successfully added contact {name}")

    return all_contacts


