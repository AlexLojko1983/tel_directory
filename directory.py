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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print('До новых встреч')
            break
