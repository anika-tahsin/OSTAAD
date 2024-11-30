def save_books(all_books):
    with open("all_books.csv", "w") as file:
        for book in all_books:
            lineWriter = f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            file.write(lineWriter)