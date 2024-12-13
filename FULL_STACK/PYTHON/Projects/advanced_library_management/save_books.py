import json
import os

def save_book(all_books):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,"all_books.json")
    with open (file_path, "w") as fp:
        json.dump(all_books,fp, indent=4)