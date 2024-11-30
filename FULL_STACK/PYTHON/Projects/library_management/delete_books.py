def delete_book(all_books):
    if all_books != []:
        choice = input("The title of the book you want to delete: ")
        if choice in all_books:
            all_books.remove
            
    else:
        print("This book doesn't exist in all books")

    print(choice, " deleted successfully")
    return all_books
    