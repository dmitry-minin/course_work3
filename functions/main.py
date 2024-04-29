from utils import *

data = get_data("./operations.json")
executed_oepeations = sortby_executed(data)
bydate_operations = sortby_date(executed_oepeations)

for i in bydate_operations[:5]:
    from_ = operation_mapping_from(i)
    to_ = operation_mapping_to(i)
    date_ = operation_mapping_date(i)
    print(f"{date_} {i.get('description')}\n"
          f"{from_} -> {to_}\n"
          f"{i.get('operationAmount').get('amount')} "
          f"{i.get('operationAmount').get('currency').get('name')}\n")

