textfile = open("file.txt", "w+")

def data():
    with open('file.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')[:-1]
        
    return data


def add_contact(contact):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        file.write('\n')

    return contact


def find_contact(data):
  command = input('Меню: \n1. Искать по ФИО \n2. Искать по номеру телефона') # view.py
  match command:
    case 1:
      find_name = input('Введите ФИО: ')
      for values in data:
        if data[values] == find_name:
          print(data[values])

    case 2:
      find_phone = input('Введите номер телефона: ')
      for values in data:
        if data[values] == find_phone:
          print(data[values])



def change_phone_number(contact):
   return None











def delete_contact(contact):
    with open("file.txt", "r+") as file:
        values = file.read().splitlines()
        flag = False
        for cont in values:
            if contact in cont:
                flag = True
                values.remove(cont)
                with open("file.txt", "w") as new_file:
                    for k in values:
                        new_file.write(k)
                        new_file.write('\n')
                view.success()
        if flag == False:
                view.not_success()

