import json
import os
import src.main


def test_book_structure():
    books = src.main.get_normalized_books_list(os.path.normpath("./testdata/books.csv"),
                                               os.path.normpath("../examples/example.json"))
    assert list(books[0].keys()) == ["title", "author", "height"]


def test_users_structure():
    users = src.main.get_normalized_users_list(os.path.normpath("./testdata/users.json"),
                                               os.path.normpath("../examples/example.json"))
    assert list(users[0].keys()) == ["name", "gender", "address"]


def test_add_one_book_for_all_users_if_books_less_then_users():
    users_with_books = src.main.main(path_to_books="./testdata/books.csv",
                                     path_to_users="./testdata/users.json",
                                     path_to_example="../examples/example.json")
    assert users_with_books[-1]["books"] == []


def test_output_structure_is_json_compitable(clean_temp_file):
    users_with_books = src.main.main(path_to_books="./testdata/books.csv",
                                     path_to_users="./testdata/users.json",
                                     path_to_example="../examples/example.json")
    with open("output_test.json", "w") as output_test:
        json.dump(users_with_books, output_test)
    with open("output_test.json", "r") as output_test:
        users_with_books_desired = json.load(output_test)
    assert users_with_books_desired == users_with_books
