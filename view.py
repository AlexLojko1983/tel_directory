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
        for i, con in book.items():
            print(f'{i:>2}.{con.get("name"):<20}:{con.get("phone"):<15}:{con.get("comment"):<20}')

    else:
        print(txt.find_message_2)


def add_contact():
    book = {key: input(value) for key, value in txt.new_contact.items()}
    return book
