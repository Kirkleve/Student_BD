from logger import input_data, print_ferst_data, print_second_data,print_parents_data, put_data, delete_data


def interface():
    print('Доброго времени суток! Это база данных учащихся!\n'
          '1. Записать данные(в 2-ух форматах)\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 4:
        print('Ты дурак?! Даю тебе последний шанс')
        command = int(input("Введите номер операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print('Выюирете файл: \n'
              '"1" - информация о студента по строчно\n'
              '"2" - информация о студентах в строку\n'
              '"3" - информация о родителях')
        choise = input('')

        while choise != '1' and choise != '2' and choise != '3':
            choise = input('"1" - информация о студента по строчно\n'
                           '"2" - информация о студентах в строку\n'
                           '"3" - информация о родителях')
        if choise == '1':
            print_ferst_data()
        elif choise == '2':
            print_second_data()
        else:
            print_parents_data()




