
from save_contacts import save_contacts

def add_contact(all_contacts):
    
    name = input("Name of the Contact person: ")
    if name.isalpha() == True:
        pass
    else:
        print("Please enter name in words")
        name = input("Name of the Contact person: ")
    
    try:
        phone_no = int(input("Phone no of the Contact person: "))
    except Exception as e:
        print("Please enter digits only for phone number")
        phone_no = int(input("Phone no of the Contact person: "))

    email = input("Email ID of the Contact person: ")
    try: 
        email.index("@")
        str(email)
        pass
    except Exception as e:
        print("Enter correct email format")
        email = input("Email ID of the Contact person: ")

    address = input("Address of the Contact person: ")

    contacts ={
        "name":name,
        "phone_no":phone_no,
        "email":email,
        "address": address
    }

    all_contacts.append(contacts)
    save_contacts(all_contacts)

    print("Successfully added contact")

    return all_contacts


