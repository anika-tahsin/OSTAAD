import json
import os

def reload_all_books(all_books):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir,"all_books.json")
    with open(file_path, "r") as fp:
        all_books = json.load(fp)

    return all_books