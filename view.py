def greetings():
    print(
        'Привет хозяин'
    )
    return greetings


def menu():
    print(
        '1 – Показать все контакты\n'
        '2 – Добавить контакт\n'
        '3 – Поиск\n'
        '4 – Изменить контакт\n'
        '5 - Удалить контакт\n'
        '6 – Выход'
    )


def error():
    print(
        'Error. Повторите ввод'
    )


def show_contacts(data):
    return data


def success():
    print(
        'Успешно'
    )
    


def not_success():
    return None




if __name__ == '__main__':
    menu()
