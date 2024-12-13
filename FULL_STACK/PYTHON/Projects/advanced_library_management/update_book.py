import datetime
import save_books

def update_book(all_books):
    search_book = input("Enter book title to update: ")
    try:
        for book in all_books:
            if book['title'] == search_book:
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                year = int(input("Enter publishing year: "))
                price = int(input("Enter Book Price: "))
                quantity = int(input("Enter Quantity Number: "))
                booklastUpdatedAt = datetime.datetime.now().strftime("%d-%m-%Y %H: %M: %S")
            
                book['title'] = title
                book['author'] = author
                book['year'] = year
                book['price'] = price
                book['quantity'] = quantity
                book['booklastUpdatedAt'] = booklastUpdatedAt

                save_books.save_book(all_books)
                print(f"Book '{book['title']}' updated successfully")
                
                return all_books
            
        print("No such book is found")
    except:  
        print("The book is not here")
    