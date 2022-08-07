from data_create import name_data, surname_data, phone_data, address_data, desk_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    desk = desk_data()
    par = input('Хотите ли добавить информацию о родителях? \n'
                'да или нет\n')
    if par == 'да':
        parents_name = name_data()
        parents_surname = surname_data()
        parents_phone = phone_data()
        with open('parents_Table.csv', 'a', encoding='UTF-8') as file:
            file.write(f'{parents_name}\n{parents_surname}\n{parents_phone}\n\n')
    else:
        print('Не забудте потом записать родителей!')

    var = int(input("В каком формате Вы хотите записать данные?\n\n"
                    "1 Вариант: Каждое наименование с новой строки\n"
                    "2 Вариант: Всё в одну строку"
                    "Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='UTF-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n{desk}\n\n')

    else:
        with open('data_second_variant.csv', 'a', encoding='UTF-8') as file:
            file.write(f'{name};{surname};{phone};{address};{desk}\n')


def print_ferst_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='UTF-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    return data_first

def print_second_data():
    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='UTF-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_second



def print_parents_data():
    with open('parents_Table.csv', 'r', encoding='UTF-8') as file:
        data_first_par = file.readlines()
        data_first_version_second_par = []
        j = 0
        for i in range(len(data_first_par)):
            if data_first_par[i] == '\n' or i == len(data_first_par) - 1:
                data_first_version_second_par.append(''.join(data_first_par[j:i + 1]))
                j = i
        data_first_par = data_first_version_second_par
        print(''.join(data_first_par))
    return data_first_par


def put_data():
    print('Из какого файла Вы хотите изменить данные?\n'
          '"1" - информация о студентах   '
          '"2" - информация о родителях ')
    choise_child_or_parents = int(input())

    while choise_child_or_parents != 1 and choise_child_or_parents != 2:
        print('"1" - информация о студентах   '
              '"2" - информация о родителях ')
        choise_child_or_parents = int(input("Введите номер варианта: "))

    if choise_child_or_parents == 1:
        print('Из какого файла вы хотите изменить ифнормацию\n'
              '"1" - из по строчного файла   "2" - из строчного файла')
        choise = int(input(''))
        while choise != 1 and choise != 2:
            choise = int(input('"1" - из по строчного файла   "2" - из строчного файла'))
        if choise == 1:
            data_first = print_ferst_data()
            print("Какую именно запись по счету Вы хотите изменить?")
            number_journal = int(input('Введите номер записи: '))
            number_journal -= 1
            print(f'Изменить данную запись\n{data_first[number_journal]}')
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            desk = desk_data()
            data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n{desk}\n\n'] + \
                         data_first[number_journal + 1:]
            with open('data_first_variant.csv', 'w', encoding='UTF-8') as file:
                file.write(''.join(data_first))
            print('Изменения успешно сохранены!')

        elif choise == 2:
            data_second = print_second_data()
            print("Какую именно запись по счету Вы хотите изменить?")
            number_journal = int(input('Введите номер записи: '))
            number_journal -= 1
            print(f'Изменить данную запись\n{data_second[number_journal]}')
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            desk = desk_data()
            data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address};{desk};\n'] + \
                          data_second[number_journal + 1:]
            with open('data_second_variant.csv', 'w', encoding='UTF-8') as file:
                file.write(''.join(data_second))
            print('Изменения успешно сохранены!')
    else:
        change_parents_data()



def change_parents_data():
    data_per = print_parents_data()
    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    print(f'Изменить данную запись\n{data_per[number_journal]}')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    data_first = data_per[:number_journal] + [f'{name}\n{surname}\n{phone}\n\n'] + \
                 data_per[number_journal + 1:]
    with open('parents_Table.csv', 'w', encoding='UTF-8') as file:
        file.write(''.join(data_first))
    print('Изменения успешно сохранены!')

def delete_data():
    print('Из какого файла Вы хотите удалить данные?\n'
          '"1" - Информация о студентах   "2" - Информация о родителях')
    choise_info = int(input(''))

    while choise_info != 1 and choise_info != 2:
        choise_info = int(input('"1" - Информация о студентах   "2" - Информация о родителях'))

    if choise_info == 1:
        number_file = int(input('Из какого файла вы хотите удалить? \n'
                                '"1" - файл с построчным выводом   "2" - строчным выводом  '))

        while number_file != 1 and number_file != 2:
            number_file = int(input('"1" - файл с построчным выводом   "2" - строчным выводом  '))

        if number_file == 1:
            data_first = print_ferst_data()
            print("Какую именно запись по счету Вы хотите удалить?")
            number_journal = int(input('Введите номер записи: '))
            print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
            data_first = data_first[:number_journal] + data_first[number_journal + 1:]
            with open('data_first_variant.csv', 'w', encoding='UTF-8') as file:
                file.write(''.join(data_first))
            print('Изменения успешно сохранены!')
        else:
            data_second = print_second_data()
            print("Какую именно запись по счету Вы хотите удалить?")
            number_journal = int(input('Введите номер записи: '))
            print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
            data_second = data_second[:number_journal] + data_second[number_journal + 1:]
            with open('data_second_variant.csv', 'w', encoding='UTF-8') as file:
                file.write(''.join(data_second))
            print('Изменения успешно сохранены!')
    else:
        data_parents = print_parents_data()
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))

        print(f'Удалить данную запись\n{data_parents[number_journal - 1]}')
        data_parents = data_parents[:number_journal] + data_parents[number_journal + 1:]
        with open('parents_Table.csv', 'w', encoding='UTF-8') as file:
            file.write(''.join(data_parents))
        print('Изменения успешно сохранены!')

