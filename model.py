import txt
import json

new_book = {}
path = 'phone.json'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        new_book = json.load(file)
    # return new_book


def save_contact():
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(new_book, file, ensure_ascii=False)


def check_id():
    if new_book:
        return max(new_book) + 1
    return 1


def add_contact(book: {int: dict[str, str]}):
    contact = {check_id(): book}
    new_book.update(contact)
