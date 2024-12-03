import csv

def get_contact(name,phone_no,email, address):
    name = input("Name of the Contact person: ")
    if name.isalpha() == True:
        pass
    else:
        print("Please enter name in words")
        name = input("Name of the Contact person: ")
    
    phone_no = int(input("Phone no of the Contact person: "))
    try:
        if phone_no.isdigit() == True:
            pass
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

    new_contact = [name, phone_no, email, address]
    contacts.append(new_contact)

def add_contacts(filename, contacts):
    with open(filename, mode='a', newline='') as myFile:
        contactWriter = csv.writer(myFile)
        contactWriter.writerow(contacts)

def is_duplicate(contacts, phone_no):
    if contacts[1] == phone_no:
        return True
    return False

