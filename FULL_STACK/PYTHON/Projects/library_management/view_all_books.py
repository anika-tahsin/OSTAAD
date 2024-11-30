def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"Title: {book['title']} \n Author: {book['author']} \n ISBN:: {book['isbn']} \n Year: {book['year']} \n Price: {book['price']} \n Quantity: {book['quantity']}\n")
    else:
        print("No books found in all books")