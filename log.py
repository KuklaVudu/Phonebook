import datetime


def import_logger(surname):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(
            f'{surname} import. Время запроса: {str(datetime.datetime.now())} \n')


def export_logger(name, surname, sec_name, phone, comment):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(
            f'{name, surname, sec_name, phone, comment} export. Время запроса: {str(datetime.datetime.now())} \n')