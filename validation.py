from view import get_message, get_view
from custom_input import choice_input, value_input

def get_obj(id, objs):
    for obj in objs:
        if obj.id == id:
            return obj
    return None

def get_obj_list(objs, isAccount=True):
    data = []
    if isAccount:
        for obj in objs:
            data.extend(obj.account)
        return data
    else:
        for obj in objs:
            data.extend(obj.transaction)
        return data

def get_obj_exist(name=None, objs=[]):
    if not objs:
        return True
    for obj in objs:
        if obj.name == name:
            print(get_message(name, 'exit'))
            return False
    return True

def get_kwargs(name, title, view_list):
    kwargs = {}
    kwargs['message'] = [name, title]
    kwargs['type'] = ['name','select']
    kwargs['title'] = title
    kwargs['view'] = view_list
    return kwargs

def get_input(kwargs):
    message = kwargs['message']
    msg_type = kwargs['type']
    title = kwargs['title']
    select_list = kwargs['view']

    name_message = get_message(message[0], msg_type[0])
    value = value_input(name_message)
    get_view(title, select_list)
    select_message = get_message(message[1], msg_type[1])
    select = choice_input(select_message)
    return (value, select)


property_type = ['Assets','Due','Liabilities']

def set_property_type(balance_sheet, select_item, created):
    if select_item == 1:
        balance_sheet.assets = created
    elif select_item == 2:
        balance_sheet.due = created
    elif select_item == 3:
        balance_sheet.liabilities = created

def get_property_type(index):
    value = property_type[index-1]
    return value
