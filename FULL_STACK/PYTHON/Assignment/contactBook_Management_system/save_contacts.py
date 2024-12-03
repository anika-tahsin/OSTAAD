
import csv
import os
def save_contacts(all_contacts):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "contacts.csv" )
    with open(file_path, "w",  newline='') as myFile:
        header = ['name', 'phone_no','email', 'address']
        headerWriter = csv.writer(myFile)
        headerWriter.writerow(header)
        for contact in all_contacts:
            lineWriter = f"{contact['name']},{contact['phone_no']},{contact['email']},{contact['address']}\n"
            print("I am writing")
            myFile.write(lineWriter)
            print(myFile)
            print("File created successfully")
    return all_contacts
          