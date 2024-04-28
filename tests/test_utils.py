import pytest
from functions.utils import *


@pytest.fixture
def data_executed():
    return [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'fault'}]

data_from1 = {"from": "Счет 77977573135347241529"}
data_from2 = {"from": "Visa Gold 7756673469642839"}
data_from3 = {"fr": " "}

data_to1 = {"to": "Счет 77977573135347241529"}
data_to2 = {"to": "Visa Gold 7756673469642839"}
data_to3 = {"fr": " "}

date_example1 = {"date": "2019-10-30T01:49:52.939296"}
date_example2 = {
    "id": 509645757,
    "state": "EXECUTED"
}

sortby_date_example = [
    {"date": "2018-06-30T02:08:58.425572"},
    {"date": "2019-08-26T10:50:58.294041"},
    {"date": "2019-07-03T18:35:29.512364"},
]
sortby_date_example_expected = [
    {"date": "2019-08-26T10:50:58.294041"},
    {"date": "2019-07-03T18:35:29.512364"},
    {"date": "2018-06-30T02:08:58.425572"}
]

def test_get_data():
    with pytest.raises(FileNotFoundError):
        get_data(None)
    assert type(get_data('test_file.json')) == list
    with pytest.raises(ValueError):
        get_data('empty_test_file.json')


def test_sortby_executed(data_executed):
    assert sortby_executed(data_executed) == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}]


def test_sortby_date():
    assert sortby_date(sortby_date_example) == sortby_date_example_expected


def test_operation_mapping_from():
    assert operation_mapping_from(data_from1) == 'Счет **1529'
    assert operation_mapping_from(data_from2) == 'Visa Gold 7756 67** **** 2839'
    assert operation_mapping_from(data_from3) == 'Поступление'


def test_operation_mapping_to():
    assert operation_mapping_to(data_to1) == 'Счет **1529'
    assert operation_mapping_to(data_to2) == 'Visa Gold 7756 67** **** 2839'
    assert operation_mapping_to(data_to3) == 'Неизвестно'


def test_operation_mapping_date():
    assert operation_mapping_date(date_example1) == '30.10.2019'
    assert type(operation_mapping_date(date_example1)) == str
    assert operation_mapping_date(date_example2) == 'Дата неизвестна'


