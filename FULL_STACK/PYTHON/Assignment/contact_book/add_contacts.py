import csv

def add_contact(filename, contact):
    """
    Add a new contact to the CSV file.
    """
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(contact)
    
def is_duplicate(contacts, phone):
    """
    # Check if a phone number already exists in the contacts.
    """ 
    for contact in contacts:
        if contact[1] == phone:
            return True
    return False

