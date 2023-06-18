import funk, txt

if __name__ == '__main__':
    while True:
        choice = funk.menu()
        match choice:
            case 1:
                funk.print_contact(funk.open_file())
            case 2:
                funk.add_contact(funk.open_file())
            case 3:
                funk.print_contact(funk.find_contact(funk.open_file()), txt.find_message_1)
            case 4:
                funk.update_contact(funk.open_file())
            case 5:
                funk.remove_contact(funk.open_file())
            case 6:
                funk.save_contact()
            case 7:
                print(txt.exit_message)
                break
