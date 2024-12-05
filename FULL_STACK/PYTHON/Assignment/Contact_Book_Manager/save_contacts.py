import csv

def save_contacts(filename, contacts):
    with open(filename, "w", newline='') as myFile:
        contactWriter = csv.writer(myFile)
        contactWriter.writerow(["Name", "Phone_No", "Email", "Address"])
        contactWriter.writerows(contacts)