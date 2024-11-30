import csv
def save_contacts(contacts):
    with open ("contacts.csv", "w") as myFile:
        contactWriter = csv.writer(myFile)
        contactWriter.writerows(contacts)
        print("File created successfully")