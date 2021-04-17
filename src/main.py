import copy
import csv
import json


def get_output_template(example_file):
    with open(example_file, "r") as example:
        example_data = json.load(example)
    return {"user": example_data.keys(), "book": example_data["books"][0].keys()}


def get_normalized_users_list(file_with_users: str) -> list:
    with open(file_with_users, "r") as users_file:
        users = json.load(users_file)
    template = get_output_template("example.json")
    return [{key: value for key, value in user.items() if key in template["user"]} for user in users]


def get_normalized_books_list(file_with_books: str) -> list:
    with open(file_with_books, newline='') as books_file:
        books = csv.DictReader(books_file)
        template = get_output_template("example.json")
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


def main():
    books = get_normalized_books_list("books.csv")
    users = get_normalized_users_list("users.json")
    return add_one_book_for_all_users(users, books)


if __name__ == "__main__":
    main()
