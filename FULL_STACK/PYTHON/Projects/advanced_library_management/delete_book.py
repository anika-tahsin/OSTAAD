import save_books

def delete_book(all_books):
    search_book = input("Enter book title to delete: ")
    for book in all_books:
        if book['title'] == search_book:
            all_books.remove(book)

            save_books.save_book(all_books)
            print("Book deleted successfully")
        
            return all_books
    
    print("Book Not Found")