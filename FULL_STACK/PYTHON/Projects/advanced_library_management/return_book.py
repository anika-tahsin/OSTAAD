
import json 
import os
import save_books
import datetime

def return_a_book(all_books):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,"all_books.json")
    with open(file_path, "r") as fp:
        all_books = json.load(fp)

    search_book = input("Enter book title to return: ").strip()


    for book in all_books:
        if book['title'].lower() == search_book.lower():
            book['quantity'] += 1
            book['bookReturnedAt'] = datetime.datetime.now().strftime("%d-%m-%Y %H: %M: %S")

            save_books.save_book(all_books)

            borrower_file_path = os.path.join(current_dir, "borrower_info.json")
            if os.path.exists(borrower_file_path):
                with open(borrower_file_path, "r") as borrower_file:
                    borrowers = json.load(borrower_file)

            borrowers = [borrower for borrower in borrowers if borrower['bookBorrowed'].lower() != search_book.lower()]
                
            with open(borrower_file_path, "w") as borrower_file:
                json.dump(borrowers, borrower_file, indent=4)

            print(f"Great! You have returned the book '{book['title']}'")
            
            return all_books
            
        
    print(f"The book '{book['title']}' is not available")
    return all_books