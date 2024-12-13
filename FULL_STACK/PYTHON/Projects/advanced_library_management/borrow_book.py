
import json 
import os
import save_books
import datetime

def borrow_book(all_books):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,"all_books.json")
    with open(file_path, "r") as fp:
        all_books = json.load(fp)

    search_book = input("Enter book title to borrow: ")

    
    for book in all_books:
        if book['title'].lower() == search_book.lower():
            if book['quantity'] != 0:
                name = input("Enter Borrower Name: ")
                phone = input("Enter Borrower Phone no: ")
                book['quantity'] -= 1
        
                
                save_books.save_book(all_books)

                borrower_data = {
                    "name": name,
                    "phone": phone,
                    "bookBorrowed": book['title'],
                    "borrowedAt": datetime.datetime.now().strftime("%d-%m-%Y %H: %M: %S"),
                    "dueDate": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%d-%m-%Y")
                }

                borrower_file_path = os.path.join(current_dir,"borrower_info.json")

                if os.path.exists(borrower_file_path):
                    with open(file_path, "r") as borrower_file:
                        borrowers = json.load(borrower_file)
                else:
                    borrowers = []
                
                borrowers.append(borrower_data)

                with open(borrower_file_path, "w") as borrower_file:
                    json.dump(borrowers, borrower_file, indent=4)
            
                print(f"You have successfully borrowed a book '{book['title']}'")
                print(f"Return it by {book['dueDate']}.")

                return all_books
            
            else:
                print(f"There are not enough book '{book['title']}' available to lend")
                return all_books