import csv
def view_contacts(contacts):
    with open ("contacts.csv", "r") as myFile:
        contactReader = csv.reader(myFile)
        for contact in contactReader:
            print(contact)