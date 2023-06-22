import txt


def menu():
    print(txt.menu[0])
    for i in range(1, len(txt.menu)):
        print(f'\t{i}. {txt.menu[i]}')
    while True:
        choice = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < len(txt.menu):
            return int(choice)
        print(txt.choice_error)


def print_contact(book: dict[int:dict[str, str]], message: str):
    if book:

        max_name = [len(cnt.get('name')) for cnt in book.values()]
        max_phone = [len(cnt.get('phone')) for cnt in book.values()]
        max_comment = [len(cnt.get('comment')) for cnt in book.values()]
        print('\n' + '-' * (max(max_name) + max(max_phone) + max(max_comment) + 7))
        for i, con in book.items():
            print(f'{i:>2}.{con.get("name"):<{max(max_name) + 1}}:'
                  f'{con.get("phone"):<{max(max_phone) + 1}}:'
                  f'{con.get("comment"):<{max(max_comment) + 1}}')
        print('-' * (max(max_name) + max(max_phone) + max(max_comment) + 7) + '\n')
    else:
        print_message(message)


def add_contact():
    book = {key: input(value) for key, value in txt.new_contact.items()}
    return book


def print_message(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def find_word() -> str:
    return input(txt.find_word)


def delete_contact():
    return input(txt.delete_id)
