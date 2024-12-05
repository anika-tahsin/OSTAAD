import csv, os

def search_contact():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "contacts.csv" )

    if not os.path.exists(file_path):
        print("No contacts found. The file does not exist.")
        return 
    
    search = input("Enter the phone number or name you want to search: ").strip().lower()
    
    try:
        with open (file_path, "r", newline='') as myFile:
            contactReader = csv.DictReader(myFile)
            result = [contact for contact in contactReader if search in contact['name'].lower() 
                      or search in contact['phone_no']]

            if result:
                print("The contact you are looking for is:\n")
                for contact in result:
                    print(f"Name: {contact['name']},Phone No: {contact['phone_no']}, Email: {contact['email']}, Address: {contact['address']}")
            else:
                print("Contact {phone_no} not found in the book")
                
                      
    except Exception as e:
        print(f"Error reading contacts- {e}")


