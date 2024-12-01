
import csv
def save_contacts(all_contacts):
    with open("contacts.csv", "w",  newline='') as myFile:
        header = ['name', 'phone_no','email', 'address']
        headerWriter = csv.writer(myFile)
        headerWriter.writerow(header)
        for contact in all_contacts:
            lineWriter = f"{contact['name']},{contact['phone_no']},{contact['email']},{contact['address']}\n"
            myFile.write(lineWriter)

          