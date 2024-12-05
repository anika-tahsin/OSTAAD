
import csv
import os
def save_contacts(all_contacts):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "contacts.csv" )
    with open(file_path, "w", newline='') as myfile:
        lineWriter = csv.DictWriter(myfile, fieldnames=["name", "phone_no", "email", "address"])
        lineWriter.writeheader()
        lineWriter.writerows(all_contacts)

    print("Contacts saved successfully.")

