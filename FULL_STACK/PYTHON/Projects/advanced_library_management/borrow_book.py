
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
            if book['quantity'] > 0:
                book['quantity'] -= 1
                book['bookBorrowedAt'] = datetime.datetime.now().strftime("%d-%m-%Y %H: %M: %S")
                
                save_books.save_book(all_books)
                print(f"You have successfully borrowed a book '{book['title']}'")
            
                return all_books
            else:
                print(f"Oh! the book '{book['title']}' is not available")
                return all_books