import json 
import os

def view_borrower():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,"borrower_info.json")
    with open(file_path, "r") as fp:
        borrowers = json.load(fp)

    if borrowers:
        for borrower in borrowers:
            print(f"Title: {borrower['bookBorrowed']} | Borrower Name: {borrower['name']} | Borrower Phone No: {borrower['phone']} | Retorn By: {borrower['bookBorrowed']}\n")
    else:
        print("No borrowers found!")
