import funk, txt
import model
import view


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                view.print_contact(model.new_book, txt.find_message_2)
            case 3:
                book = view.add_contact()
                model.add_contact(book)
            case 4:
                funk.update_contact(funk.open_file())
            case 5:
                funk.remove_contact(funk.open_file())
            case 6:
                pass
            case 7:
                model.save_contact()
            case 8:
                print(txt.exit_message)
                break
