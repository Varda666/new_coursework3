import json
from datetime import datetime

def get_all_data_from_operations():
    '''Получение всей информации из файла operations.json'''
    f = open("..\\src\\operations.json", 'r', encoding="utf-8")
    file = json.load(f)
    return file
# def get_data_from_operations():
#     '''Получение информации об одной операции из файла operations.json'''
#     f = open("operations.json", 'r', encoding="utf-8")
#     file = json.load(f)
#     for dicts_ in file:
#         return dicts_




def get_datetime_from_operations_date(get_all_data_from_operations):
    """Получение даты в виде строки и приведение ее в формат datetime"""
    datetime_list = []
    for dicts_ in get_all_data_from_operations:
        if 'date' in dicts_:
            date_time_str = dicts_["date"]
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f')
            # datetime_list.append(date_time_obj.date())
            datetime_list.append(date_time_obj)
        else:
            pass
    return datetime_list


def sorted_operations_date(get_all_data_from_operations):
    """Получает даты последних 5 операций в формате datetime"""
    sorted_date_dttm_list = sorted(get_datetime_from_operations_date(get_all_data_from_operations), reverse=True)
    return sorted_date_dttm_list[:5]

def get_need_data_from_operations(get_all_data_from_operations):
    """Получает список словарей с информацией о последних 5 операциях"""
    need_data_dict_list = []
    for dict_ in get_all_data_from_operations:
        if 'date' in dict_:
            date_time_str = dict_["date"]
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f')
            for item in sorted_operations_date(get_all_data_from_operations):
                if item == date_time_obj:
            #
            # if date_time_obj in sorted_operations_date():
                    need_data_dict_list.append(dict_)
            else:
                pass
        else:
            pass
    return need_data_dict_list


    # for item in get_datetime_from_operations_date(get_all_data_from_operations):
    #     if item in sorted_operations_date(get_all_data_from_operations):
    #         print(item)

def get_datetime_from_operations_date_for_conversion(dicts_):
    """Получение даты в виде строки и приведение ее в формат, как в задании"""
    # for dicts_ in get_all_data_from_operations():
    if 'date' in dicts_:
        date_time_obj = datetime.strptime(dicts_["date"], '%Y-%m-%dT%H:%M:%S.%f')
        date_time_obj_for_conversion = date_time_obj.date()
        current_date_string = date_time_obj_for_conversion.strftime('%d.%m.%Y')
        return current_date_string
    else:
        pass


def get_from_from_operations_for_transformation(dicts_):
    """Получение информации откуда осуществлен перевод"""
    # # ls_from = []
    # for dicts_ in get_all_data_from_operations():
    if "from" in dicts_:
        if 'Счет' in dicts_["from"]:
            return f'Счет {dicts_["from"][-4:]}'
        elif 'Classic' in dicts_["from"]:
            return f'Visa Classic {dicts_["from"][-16:-10]}** ****{dicts_["from"][-4:]}'
        elif 'Gold' in dicts_["from"]:
            return f'Visa Gold {dicts_["from"][-16:-10]}** ****{dicts_["from"][-4:]}'
        elif 'МИР' in dicts_["from"]:
            return f'МИР {dicts_["from"][-16:-10]}** ****{dicts_["from"][-4:]}'
        elif 'MasterCard' in dicts_["from"]:
            return f'MasterCard {dicts_["from"][-16:-10]}** ****{dicts_["from"][-4:]}'
        elif 'Platinum' in dicts_["from"]:
            return f'Visa Platinum {dicts_["from"][-16:-10]}** ****{dicts_["from"][-4:]}'
        elif 'Maestro' in dicts_["from"]:
            return f'Maestro {dicts_["from"][-16:-10]}** ****{dicts_["from"][-4:]}'
        else:
            return ('Не указано')
    else:
        return ('Не указано')


    # # print(ls_from)
    # new_ls_from = []
    # for item in ls_from:
    #     if 'Visa' in item:
    #         new_ls_from.append(item.split(" ")[1])
    #     else:
    #         new_ls_from.append(item.split(" ")[0])
    # print(list(set(new_ls_from)))
    # if


def get_to_from_operations_for_transformation(dicts_):
    """Получение информации куда осуществлен перевод"""
    # for dicts_ in get_all_data_from_operations():
    if "to" in dicts_:
        if 'Счет' in dicts_["to"]:
            return f'Счет **{dicts_["to"][-4:]}'
        elif 'Classic' in dicts_["to"]:
            return f'Visa Classic {dicts_["to"][-16:-10]}** ****{dicts_["to"][-4:]}'
        elif 'Gold' in dicts_["to"]:
            return f'Visa Gold {dicts_["to"][-16:-10]}** ****{dicts_["to"][-4:]}'
        elif 'МИР' in dicts_["to"]:
            return f'МИР {dicts_["to"][-16:-10]}** ****{dicts_["to"][-4:]}'
        elif 'MasterCard' in dicts_["to"]:
            return f'MasterCard {dicts_["to"][-16:-10]}** ****{dicts_["to"][-4:]}'
        elif 'Platinum' in dicts_["to"]:
            return f'Visa Platinum {dicts_["to"][-16:-10]}** ****{dicts_["to"][-4:]}'
        elif 'Maestro' in dicts_["to"]:
            return f'Maestro {dicts_["to"][-16:-10]}** ****{dicts_["to"][-4:]}'
        else:
            pass
    else:
        pass


def get_amount_and_cur_name_from_operations_for_transformation(dicts_):
    """Получение информации о сумме и валюте"""
    # for dicts_ in get_all_data_from_operations():
    return (f'{dicts_["operationAmount"]["amount"]} {dicts_["operationAmount"]["currency"]["name"]}')



def get_five_last_operations():
    for i in get_need_data_from_operations(get_all_data_from_operations()):
        print(f"""{get_datetime_from_operations_date_for_conversion(i)}  
{get_from_from_operations_for_transformation(i)} {get_to_from_operations_for_transformation(i)}
{get_amount_and_cur_name_from_operations_for_transformation(i)} \n """)

get_five_last_operations()



