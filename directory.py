new_book = {}


def open_file(path='phone.txt'):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for con in data:
            nc = con.strip().split(':')
            new_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    return new_book


def print_contact(book: dict[int, dict], message: str = 'Справочник загружен!!!'):
    print(message)
    print('-' * 60)
    for i, con in book.items():
        str_con = f'{i:>2}. {con.get("name"):<20}:{con.get("phone"):<15}:{con.get("comment"):<20}'
        print(str_con)
    print('-' * 60)


def add_contact(book: dict[int, dict]):
    book[max(book.keys()) + 1] = {'name': input('Введите ФИО: '),
                                  'phone': input('Введите номер телефона: '), 'comment': input('Комментарий: ')}


def find_contact(book: dict[int, dict]):
    res = {}
    self = input('Введите параметр поиска: ')
    for i, con in book.items():
        if self.lower() in ' '.join(list(con.values())).lower():
            res[i] = con
    return res


def remove_contact(book: dict[int, dict]):
    id_con = int(input('Введите Ид контакта, который надо удалить: '))
    if min(book.keys()) <= id_con <= max(book.keys()):
        book.pop(id_con)
        print_contact(book, 'Остались контакты !!!')
    else:
        print('Такого контакта нет')

def save_contact():
    pass



def menu():
    menu = '''Главное меню
    1. Открыть справочник
    2. Добавить контакт
    3. Найти контакт
    4. Редактировать контакт
    5. Удалить контакт
    6. Сохранить справочник
    7. Выйти'''
    print(menu)

    while True:
        choice = input('Выберите действие: ')
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        print('Выберите все таки действие: ')


while True:
    choice = menu()
    match choice:
        case 1:
            print_contact(open_file())
        case 2:
            add_contact(open_file())
        case 3:
            print_contact(find_contact(open_file()), 'Возможно вы искали?')
        case 4:
            pass
        case 5:
            remove_contact(open_file())
        case 6:
            pass
        case 7:
            print('До новых встреч')
            break
