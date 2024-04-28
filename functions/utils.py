import json
from datetime import datetime


def get_data(file_path: str) -> list[dict]:
    if not file_path:
        raise FileNotFoundError("Empty path")
    with open(file_path) as f:
        lst_of_dicts = json.load(f)
        if not lst_of_dicts:
            raise ValueError("Empty file")
    return lst_of_dicts


def sortby_executed(array: list[dict]) -> list[dict]:
    sorted_status = []
    for i in array:
        i_array = str(i.get('state'))
        if i_array.upper() == 'EXECUTED':
            sorted_status.append(i)
    return sorted_status


def sortby_date(list_of_dicts: list[dict]) -> list[dict]:
    sorted_list = sorted(list_of_dicts, key=lambda k: k['date'], reverse=True)
    return sorted_list


def operation_mapping_from(operation: dict) -> str or None:
    from_ = operation.get('from')
    if not from_:
        return "Поступление"
    elements_from = from_.split(' ')
    pay_type_from = ' '.join(elements_from[:-1])
    number_from = elements_from[-1]
    if len(number_from) == 16:
        return f'{pay_type_from} {number_from[:4]} {number_from[4:6]}** **** {number_from[-4:]}'
    else:
        return f'{pay_type_from} **{number_from[-4:]}'


def operation_mapping_to(operation: dict) -> str or None:
    to_ = operation.get('to')
    if not to_:
        return 'Неизвестно'
    elements_to = to_.split(' ')
    pay_type_to = ' '.join(elements_to[:-1])
    number_to = elements_to[-1]
    if len(number_to) == 16:
        return f'{pay_type_to} {number_to[:4]} {number_to[4:6]}** **** {number_to[-4:]}'
    else:
        return f'{pay_type_to} **{number_to[-4:]}'


def operation_mapping_date(operation: dict) -> datetime or None:
    date = operation.get('date')
    if not date:
        return "Дата неизвестна"
    dt_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return dt_date.strftime('%d.%m.%Y')
