import csv 

def view_contacts(filename):
    try:
        with open(filename, "r") as myFile:
            contactReader = csv.reader(myFile)
            next(contactReader) # skipping header row
            return list(contactReader)
    except Exception as e:
        print("No file found")
        return []
    
def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!")

    else:
        print("\nAll contacts: ")
        print('-'*50)
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. 'Name': {contact[0]}, 'Phone_No':{contact[1]} , 'Email':{contact[2]}, 'Address':{contact[3]}")
        print('-'*50)

    
