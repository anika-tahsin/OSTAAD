from save_books import save_books

def update_books(all_books):
    if not all_books:
        print("No books to update")
        return all_books
    # Show all books
    print("\n Available books")
    for i, book in enumerate(all_books, start=1):
        print(f'{i}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, {book['price']}')

    # Choose a book to update
    try: 
        choice = int(input("\n Enter book number to update: ")).strip()
        if choice < 1 or choice > len(all_books):
            print("Invalid choice")
            return all_books
    except ValueError:
        print("Enter valid number")
        return all_books
    
    selected_book = all_books[choice-1]

    print("\n Fields to update")
    fields = list(selected_book.keys())
    for i, field in enumerate(fields, start=1):
        print(f'{i}. {field}')

    # Select a field to update
    try: 
        field_choice = int(input("\n Enter filed to update: ")).strip()
        if field_choice < 1 or field_choice > len(fields):
            print("Invalid choice")
            return all_books
    except ValueError:
        print("Enter valid number")
        return all_books

    field_to_update = fields[field_choice-1]

    new_value = input(f'Enter the new value for {field_to_update}')

    # Update the field
    if field_to_update in ["year", "price", "quantity"]:  # Numeric fields
        try:
            new_value = int(new_value) if field_to_update != "price" else float(new_value)
        except ValueError:
            print(f"Invalid input for {field_to_update}. Update failed.")
            return all_books

    selected_book[field_to_update] = new_value
    save_books(all_books)

    print("\nBook updated successfully!")
    return all_books