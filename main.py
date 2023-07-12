def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Закончить работу")
    choice = int(input())
    return choice


def print_result(phone_book):
    for i in phone_book:
        for key in i.keys():
            print(f'|{key.rjust(20)}|', end='')
        print()    
        print('----------------------------------------------------------------------------------------')
        break
    for i in phone_book:
        for value in i.values():
            print(f'|{value.rjust(20)}|', end='')
        print()


def get_search_name():
    return input("Введите фамилию для поиска: ")


def find_by_name(phone_book, name):
    for i in phone_book:
        for key in i.keys():
            print(f'|{key.rjust(20)}|', end='')
        print()    
        print('----------------------------------------------------------------------------------------')
        break
    for i in phone_book:
        for key, value in i.items():
            if key == 'Фамилия':
                if value.lower() == name.lower():
                    for value in i.values():
                        print(f'|{value.rjust(20)}|', end='')
                break        


def get_search_number():
    a = input("Введите номер: ")
    if a.isdigit():
        return int(a)
    else:
        print("Вы ввели не номер, попробуйте еще раз")
        return get_search_number() 


def find_by_number(phone_book, number):
    for i in phone_book:
        for key in i.keys():
            print(f'|{key.rjust(20)}|', end='')
        print()    
        print('----------------------------------------------------------------------------------------')
        break
    for i in phone_book:
        for key, value in i.items():
            if key == 'Телефон':
                if int(value) == number:
                    print(value)
                    for value in i.values():
                        print(f'|{value.rjust(20)}|', end='')
            

def get_new_user():
    new_user  = input("Введите фамилию пользователя ") + ","
    new_user += input("Введите имя пользователя ") + ","
    new_user += input("Введите номер телефона пользователя ") + ","
    new_user += input("Введите примечание ") + "\n"
    
    return new_user


def add_user(filename ,user_data):
    with open(filename, 'a+', encoding='utf-8') as fout:
        fout.write(user_data)
        

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phon.txt')


    while (choice != 5):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            find_by_name(phone_book, name)
        elif choice == 3:
            number = get_search_number()
            find_by_number(phone_book, number)
        elif choice == 4:
            user_data = get_new_user()
            add_user('phon.txt',user_data)
            phone_book = read_csv('phon.txt')
        elif choice > 5:
            print("Вы ввели слишком большое значение, попробуйте еще раз ")
            print()
        choice = show_menu()


def read_csv(filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data        
            
           
def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')     


work_with_phonebook()    
