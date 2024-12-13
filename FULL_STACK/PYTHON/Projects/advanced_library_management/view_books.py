import json 
import os

def view_all_books(all_books):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,"all_books.json")
    with open(file_path, "r") as fp:
        all_books = json.load(fp)

    if all_books != []:
        for book in all_books:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN:: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | bookAddedAt: {book['bookAddedAt']} | Book last Updated At: {book['booklastUpdatedAt']} | Book borrowed at: {book['bookBorrowedAt']} | Book returned at: {book['bookReturnedAt']}\n")
    else:
        print("No books found!")
