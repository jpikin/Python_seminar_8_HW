def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
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
        for value in i.values():
            if name in value:
                for value in i.values():
                    print(f'|{value.rjust(20)}|', end='')
            print()
            break
                            


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phon.txt')


    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            find_by_name(phone_book, name)
        # elif choice == 3:
        #     number = get_search_number()
        #     print(find_by_number(phone_book, number))
        # elif choice == 4:
        #     user_data = get_new_user()
        #     add_user(phone_book, user_data)
        #     write_csv('phonebook.csv', phone_book)
        # elif choice == 5:
        #     file_name = get_file_name()
        #     write_txt(file_name, phone_book)
        choice = show_menu()

def read_csv(filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data        
            
           

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')     







work_with_phonebook()    
