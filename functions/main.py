from utils import *

data = get_data("./operations.json")
executed_oepeations = sortby_executed(data)
bydate_operations = sortby_date(executed_oepeations)

for i in bydate_operations[:5]:
    """Данный цикл перебирает список словарей,
    с заранее отфильтрованными по статусу Executed
    и дате операциями, и применяет к ним  функции описанные в файле utils.
    Функции берут следующие данные из словаря: дата перевода, описание перевода,
    откуда, куда, сумма перевода, валюта; и преобразуют их в необходимый формат
    """
    from_ = operation_mapping_from(i)
    to_ = operation_mapping_to(i)
    date_ = operation_mapping_date(i)
    print(f"{date_} {i.get('description')}\n"
          f"{from_} -> {to_}\n"
          f"{i.get('operationAmount').get('amount')} "
          f"{i.get('operationAmount').get('currency').get('name')}\n")

