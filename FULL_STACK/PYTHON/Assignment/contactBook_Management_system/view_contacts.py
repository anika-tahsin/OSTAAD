import csv, os
# import save_contacts
def view_contacts(all_contacts):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "contacts.csv" )
    
    with open (file_path, "r") as myFile:
        contactReader = csv.reader(myFile)
        for contact in contactReader:
            print(contact)

    return all_contacts



