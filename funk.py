import txt
new_book = {}


def menu():
    print(txt.menu)

    while True:
        choice = input(txt.choice_1)
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        print(txt.choice_2)


# def open_file(path='phone.txt'):
#     with open(path, 'r', encoding='UTF-8') as file:
#         data = file.readlines()
#         for con in data:
#             new_con = con.strip().split(':')
#             new_book[int(new_con[0])] = {'name': new_con[1],
#                                          'phone': new_con[2],
#                                          'comment': new_con[3]
#                                          }
#     return new_book


# def print_contact(book: dict[int, dict], message: str = txt.message_print):
#     if len(book) == 0:
#         print(txt.find_message_2)
#     else:
#         print(message)
#         print('-' * 60)
#         for i, con in book.items():
#             str_con = f'{i:>2}.{con.get("name"):<20}:{con.get("phone"):<15}:{con.get("comment"):<20}'
#             print(str_con)
#         print('-' * 60)


# def add_contact(book: dict[int, dict]):
#     book[max(book.keys()) + 1] = {'name': input(txt.name),
#                                   'phone': input(txt.phone),
#                                   'comment': input(txt.comment)
#                                   }


def find_contact(book: dict[int, dict]):
    res = {}
    self = input(txt.find_word)
    for i, con in book.items():
        if self.lower() in ' '.join(list(con.values())).lower():
            res[i] = con
    return res


def remove_contact(book: dict[int, dict]):
    id_con = int(input(txt.delete_id))
    if min(book.keys()) <= id_con <= max(book.keys()):
        book.pop(id_con)
        print_contact(book, txt.message_remove)
        print(txt.download_directory)
    else:
        print(txt.error_contact)


# def save_contact(path='phone.txt'):
#     with open(path, 'w', encoding='UTF-8') as file:
#         for i, con in new_book.items():
#             str_con = f'{str(i)}:{con.get("name")}:{con.get("phone")}:{con.get("comment")}\n'
#             file.write(str_con)


def update_contact(book: dict[int, dict]):
    id_con = int(input(txt.update_id))
    if min(book.keys()) >= id_con <= max(book.keys()):
        book[id_con] = {'name': input(txt.name),
                        'phone': input(txt.phone),
                        'comment': input(txt.comment)
                        }
    else:
        print(txt.error_contact)
