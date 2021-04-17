import json
import src.main


def test_book_structure():
    books = src.main.get_normalized_books_list("books.csv")
    assert list(books[0].keys()) == ["title", "author", "height"]


def test_users_structure():
    users = src.main.get_normalized_users_list("users.json")
    assert list(users[0].keys()) == ["name", "gender", "address"]


def test_add_one_book_for_all_users_if_books_less_then_users():
    users_with_books = src.main.main()
    assert users_with_books[-1]["books"] == []


def test_output_structure_is_json_compitable(clean_temp_file):
    users_with_books = src.main.main()
    with open("output_test.json", "w") as output_test:
        json.dump(users_with_books, output_test)
    with open("output_test.json", "r") as output_test:
        users_with_books_desired = json.load(output_test)
    assert users_with_books_desired == users_with_books
