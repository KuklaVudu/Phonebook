import log as log


def inp_mod():
    mod = input('Введите режим работы (импорт или экспорт): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    log.import_logger(surname)
    return surname


def view_import(result):
    print(*result, sep='\n')


def inp_export():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    sec_name = input('Введите отчество: ')
    phone = input('Введите телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    log.export_logger(name, surname, sec_name, phone, comment)
    return '\n', name, surname, sec_name, phone, comment


def view_import_no():
    print(f'Данные не найдены')