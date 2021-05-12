import copy
import csv
import json
import os


def get_output_template(example_file):
    with open(example_file, "r") as example:
        example_data = json.load(example)
    return {"user": example_data.keys(), "book": example_data["books"][0].keys()}


def get_normalized_users_list(file_with_users: str, file_with_example: str) -> list:
    with open(file_with_users, "r") as users_file:
        users = json.load(users_file)
    template = get_output_template(file_with_example)
    return [{key: value for key, value in user.items() if key in template["user"]} for user in users]


def get_normalized_books_list(file_with_books: str, file_with_example: str) -> list:
    with open(file_with_books, newline='') as books_file:
        books = csv.DictReader(books_file)
        template = get_output_template(file_with_example)
        return [{key.lower(): value for key, value in book.items() if key.lower() in template["book"]} for book in books]


def add_one_book_for_all_users(users: list, books: list) -> list:
    _users = copy.deepcopy(users)
    _books = copy.deepcopy(books)
    for user in _users:
        try:
            user["books"] = [_books.pop()]
        except IndexError:
            user["books"] = []
    return _users


def main(path_to_books="../examples/books.csv",
         path_to_users="../examples/users.json",
         path_to_example="../examples/example.json"):
    books = get_normalized_books_list(os.path.normpath(path_to_books), os.path.normpath(path_to_example))
    users = get_normalized_users_list(os.path.normpath(path_to_users), os.path.normpath(path_to_example))
    return add_one_book_for_all_users(users, books)


if __name__ == "__main__":
    result = main()
    if os.path.isfile("./result.json"):
        os.remove("./result.json")

    with open("result.json", "w") as output:
        json.dump(result, output)
    print("File result.json was created.")
