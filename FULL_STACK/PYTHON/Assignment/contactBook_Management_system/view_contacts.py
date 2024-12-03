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

""" 
import csv

def view_contacts(filename):
    """
    # Load contacts from a CSV file and return them as a list of lists.
    """
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            return list(reader)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

"""

