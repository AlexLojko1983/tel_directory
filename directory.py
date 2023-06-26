import funk, txt
import model
import view


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                if model.open_file():
                    view.print_message(txt.message_print)
                else:
                    view.print_message(txt.message_print_err)
            case 2:
                view.print_contact(model.new_book, txt.find_message_2)
            case 3:
                book = view.add_contact()
                model.add_contact(book)
                view.print_message(txt.add_successful(book.get('name')))
            case 4:
                word = view.find_word()
                result = model.find_contact(word)
                view.print_contact(result, txt.find_message_1)
            case 5:
                number = view.delete_contact()
                book = view.add_contact()
                model.update_contact(book, number)
            case 6:
                number = view.delete_contact()
                if model.delete_contact(number):
                    view.print_message(txt.del_message)
                else:
                    view.print_message(txt.not_del_message)
            case 7:
                if model.save_contact():
                    view.print_message(txt.download_directory)
                else:
                    view.print_message(txt.err_download_directory)

            case 8:
                view.print_message(txt.exit_message)
                break
