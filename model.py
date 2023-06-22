import txt
import json

new_book = {}
path = 'phone.json'


def open_file():
    global new_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            new_book = json.load(file)
            return True
    except:
        return False


def save_contact():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(new_book, file, ensure_ascii=False)
            return True
    except:
        return False


def check_id():
    if new_book:
        return int(max(new_book)) + 1
    return 1


def add_contact(book: {int: dict[str, str]}):
    contact = {check_id(): book}
    new_book.update(contact)


def find_contact(word: str) -> dict[int:dict[str, str]]:
    result = {}
    for i, cnt in new_book.items():
        if word.lower() in ' '.join(cnt.values()).lower():
            result[i] = cnt
    return result


def delete_contact(number: str):
    try:
        del new_book[number]
        return True
    except:
        return False


def update_contact(book, number: str):
    try:
        new_book[number] = {book}
        return True
    except:
        return False
