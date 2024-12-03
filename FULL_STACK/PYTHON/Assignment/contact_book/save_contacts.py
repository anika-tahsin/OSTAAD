import csv

def save_contacts(filename, contacts):
    """
    Save all contacts to a CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address"])  # Header row
        writer.writerows(contacts)
