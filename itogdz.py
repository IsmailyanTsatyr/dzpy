phone_book = {}

def open_file(path: str = 'tel.txt'):
    phone_book.clear()
    file = open(path, 'r' , encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone' : nc[2] , 'comment' : nc[3]}
    print('\nТелефонная книга загруженна!')


def show_contacts(book: dict[int,dict]):
    print('\n' + '=' * 200)   
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')



def add_contact():
    uid = max(list(phone_book.keys())) + 1 
    
    name = input('Введите имя контакта : ')
    phone = input('Введите номер контакта : ')
    comment = input('Введите комментарий к контакту : ')
    phone_book[uid] = {'name ': name , 'phone' : phone,'comment':comment  } 

    print(f'\nКонтакт {name} успешно дабавлен!')






def menu() -> int:
    main_menu = ''' Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход '''
    print(main_menu)
    while True:
        select = input('  Выберетие пункт меню')
        if select.isdigit() and 0 < int(select)<9:
            return int (select)
        print(' Ошибка ввода введите число от 1 до 8')
    
    

    
open_file()    
while True:
    select = menu()
    match select:
        case 1 :
            open_file()
        case 2 :
            pass
        case 3 :
            show_contacts(phone_book)
        case 4 :
            add_contact()
        case 5 :
            pass
        case 6 :
            pass
        case 7 :
            pass
        case 8 :
            print(' До свидания ')  
            break

