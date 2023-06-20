import json
from src import functons
import pytest
import datetime

@pytest.fixture
def get_all_data_from_operations():
    f = open("..\\src\\operations.json", 'r', encoding="utf-8")
    file = json.load(f)
    return file

@pytest.fixture
def get_dicts_():
    f = open("..\\src\\operations.json", 'r', encoding="utf-8")
    file = json.load(f)
    for dict_ in file:
        return dict_


@pytest.fixture
def get_dicts_0():
    f = open("..\\src\\operations.json", 'r', encoding="utf-8")
    file = json.load(f)
    return file[0]
def test_get_all_data_from_operations():
    assert (type(functons.get_all_data_from_operations())) == list


def test_get_datetime_from_operations_date(get_dicts_0):
    assert functons.get_datetime_from_operations_date(get_dicts_0) == dict
def test_get_datetime_from_operations_date_type_error(get_all_data_from_operations):
    with pytest.raises(TypeError):
        functons.get_datetime_from_operations_date(get_all_data_from_operations)
def test_sorted_operations_date():
    assert len(functons.sorted_operations_date()) == 5

def test_get_need_data_from_operations(get_all_data_from_operations):
    assert len(functons.get_need_data_from_operations(get_all_data_from_operations)) == 5

def test_get_datetime_from_operations_date_for_conversion(get_dicts_):
    assert type(functons.get_datetime_from_operations_date_for_conversion(get_dicts_)) == str

def test_get_from_from_operations_for_transformation(get_dicts_0):
    assert functons.get_from_from_operations_for_transformation(get_dicts_0) == "Maestro 159683** ****5199"

def test_get_to_from_operations_for_transformation(get_dicts_0):
    assert functons.get_to_from_operations_for_transformation(get_dicts_0) == "Счет **9589"
    assert type(functons.get_to_from_operations_for_transformation(get_dicts_0)) == str

def test_get_amount_and_cur_name_from_operations_for_transformation(get_dicts_0):
    assert functons.get_amount_and_cur_name_from_operations_for_transformation(get_dicts_0) == '31957.58 руб.'

