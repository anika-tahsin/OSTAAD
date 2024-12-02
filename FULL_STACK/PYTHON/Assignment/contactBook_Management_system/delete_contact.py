
import csv
def delete_contact(all_contacts):
    with open("contacts.csv", "r") as myFile:
        print(all_contacts)
        for contact in all_contacts:
            choice = input("The name of the contact you want to delete: ")
            if choice in all_contacts:
                all_contacts.remove
            else:
                print("The contact is not in the contact book")
            print(choice, " deleted successfully")
    return all_contacts