import csv
def view_contacts(contacts):
    with open ("F:\Syncing\PROGRAMMING\OSTAAD\FULL_STACK\PYTHON\Assignment\contactBook_Management_system\contacts.csv", "r") as myFile:
        contactReader = csv.reader(myFile)
        for contact in contactReader:
            print(contact)