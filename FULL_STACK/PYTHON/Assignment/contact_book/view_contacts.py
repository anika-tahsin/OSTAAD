import csv

def view_contacts(filename):
    """
    Load contacts from a CSV file and return them as a list of lists.
    """
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            return list(reader)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
