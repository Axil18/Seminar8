import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        if answer == '1':
            date = model.show_contacts()
            view.show_contacts(date)
        elif answer == '2':
            contact = input('Введите данные контакта через пробел: ')
            res = model.add_contact(contact)
            if res:
                view.success()
            else:
                view.not_success()
        elif answer == '3':
            contact = model.find_contact
            res = model.find_contact(contact)
            view.show_contacts(res)
        elif answer == '4':
            contact = input('Введите имя и фамилию контакта для изменения: ')
            res = model.change_phone_number(contact)
            view.show_contacts(res)
        elif answer == '5':
            contact = input('Введите имя и фамилию для удаления контакта: ')
            res = model.delete_contact(contact)
            view.show_contacts(res)
        elif answer == '6':
            break
        else:
            view.error()
