import csv
def search_contact(all_contacts):
    with open ("contacts.csv", "r") as myFile:
        contactReader = csv.reader(myFile)
        for contact in contactReader:
            choice = input("Please enter the contact name you want to search: ")
            if choice in contact[0].find(choice):
                print(contact)
            else:
                print("The contact is not in the book")
    return all_contacts