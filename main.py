from datetime import date, timedelta

from view import ConsoleView, get_message, get_view
from custom_input import choice_input
from models import BalanceSheet, Category, Account, Transaction
from validation import (
    get_obj, get_obj_exist, get_kwargs, get_input, get_obj_list,
    property_type, set_property_type, get_property_type
    )
from db_manager import CsvFileReadWrite, init_write, init_read, init_file

console_view_items = {
    'app':['Category','Account','Transaction', 'Report']
}
cud = ['Create','Update','Delete']

def main():
    init_write()
    balance_sheet = init_read()
    print()
    while True:
        # init console  view
        console_view = ConsoleView()
        console_view.header_view
        console_view.sub_title = console_view_items['app']
        console_view.content_view(False)
        #choice message and input
        input_message = get_message(msg_type='choice')
        choice = choice_input(input_message)
        if choice == 0:
            break
        # Category
        if choice == 1:
            while True:
                category_file = CsvFileReadWrite('./db/category.csv', 'r')
                get_view('Category', cud)
                choice = choice_input(input_message)
                if choice == 0:
                    category_file.close()
                    break
                # Create category
                if choice == 1:
                    if not property_type:
                        message = get_message('Property Type', 'not availabel')
                        print(message)
                        break
                    
                    # header view
                    console_view.header_view
                    # set input kwargs
                    input_kwargs = get_kwargs('Category', 'Property Type', property_type)
                    # get value and select property item
                    value, select_item = get_input(input_kwargs)
                    # get property value
                    category_property_type = get_property_type(select_item)
                    
                    # object availabel or not
                    category_list = balance_sheet.get_list()
                    if get_obj_exist(value, category_list):
    
                        # category created
                        created = Category(value, category_property_type)
                       
                        # category file write
                        category_file.set_mode('a')
                        category_file.write(created.get_data())
                        set_property_type(balance_sheet, select_item, created)
                # update category
                elif choice == 2:
                    # object availabel or not
                    category_list = balance_sheet.get_list()
                    if not category_list:
                        # message view
                        message = get_message('Category', 'not availabel')
                        print(message)
                        break
                    
                    # updating data choice
                    get_view('Account Category', category_list)
                    input_message = get_message('Account Category', 'select')
                    select_item = choice_input(input_message)
                    if select_item == 0:
                        break
                    # get object to update
                    obj = get_obj(select_item, category_list)
                    
                    # header view
                    console_view.header_view
                    # set input kwargs
                    input_kwargs = get_kwargs('Category', 'Property Type', property_type)
                    # get value and select property item
                    value, select_item = get_input(input_kwargs)
                    # get property value
                    category_property_type = get_property_type(select_item)
                    
                    # object availabel or not
                    if get_obj_exist(value, category_list):
                        
                        # category update
                        obj.name = value
                        obj.property_type = category_property_type
                        
                        # write category file
                        category_file.set_mode('w')
                        elems = ['sn','name','pro_type']
                        category_file.write(elems)
                        for category in category_list:
                            category_file.write(category.get_data())
                # delete object
                elif choice == 3:
                    console_view.header_view
                # not found choice
                else:
                    message = get_message(msg_type='wrong')
                    print(message)
        # Account
        elif choice == 2:
            while True:
                account_file =  CsvFileReadWrite('./db/account.csv', 'r')
                get_view('Account', cud)
                choice = choice_input(input_message)
                if choice == 0:
                    account_file.close()
                    break
                
                # create account
                if choice == 1:
                    category_list = balance_sheet.get_list()
                    if not category_list:
                        message = get_message('Category', 'not availabel')
                        print(message)
                        break
                    
                    console_view.header_view
                    # set input kwargs
                    input_kwargs = get_kwargs('Account', 'Account Category', category_list)
                    # get value and select property item
                    value, select_item = get_input(input_kwargs)
                    # get account list
                    account = get_obj_list(category_list)
                   
                    if get_obj_exist(value, account):
                       
                        created = Account(value, select_item)
                        
                        #account file write
                        account_file.set_mode('a')
                        account_file.write(created.get_data())
                        category = get_obj(select_item, category_list)
                        category.account = created

                # update account
                elif choice == 2:
                    category_list = balance_sheet.get_list()
                    account_list = get_obj_list(category_list)
                    if not category_list:
                        message = get_message('Category', 'not availabel')
                        print(message)
                        break 
                    
                    get_view('Category', category_list)
                    input_message = get_message('category', 'select')
                    select_item = choice_input(input_message)
                    if select_item == 0:
                        break
                    # get object to update
                    category = get_obj(select_item, category_list)
                    tem_account_list = category.account
                    if not tem_account_list:
                        message = get_message('Account', 'not availabel')
                        print(message)
                        break 
                    # updating data choice
                    console_view.header_view
                    print('  Account')
                    for account in tem_account_list:
                        print(f'    {account.id}: {account.name}')
                    input_message = get_message('Account', 'select')
                    select_item = choice_input(input_message)
                    if select_item == 0:
                        break
                    # get object to update
                    obj = get_obj(select_item, account_list)

                    console_view.header_view
                    # set input kwargs
                    input_kwargs = get_kwargs('Account', 'Account Category', category_list)
                    # get value and select property item
                    value, select_item = get_input(input_kwargs)
                    
                    # update account here
                    if get_obj_exist(value, account_list):
                        
                        obj.name = value
                        obj.category_id = select_item
                        
                        account_file.set_mode('w')
                        elems = ['sn','name','category_id']
                        account_file.write(elems)
                        for account in account_list:
                            account_file.write(account.get_data())

                elif choice == 3:
                    console_view.header_view
                else:
                    message = get_message(msg_type='wrong')
                    print(message)
        # Transaction
        elif choice == 3:
            while True:
                transaction_file = CsvFileReadWrite('./db/transaction.csv', 'r')
                category_list = balance_sheet.get_list()
                if not category_list:
                    # message view
                    message = get_message('Category', 'not availabel')
                    print(message)
                    break

                get_view('Category', cud)
                choice = choice_input(input_message)
                if choice == 0:
                    transaction_file.close()
                    break

                if choice == 1:
                    get_view('Category', category_list)
                    input_message = get_message('category', 'select')
                    select_item = choice_input(input_message)
                    if select_item == 0:
                        break
                    # get object to update
                    category = get_obj(select_item, category_list)
                    tem_account_list = category.account
                    if not tem_account_list:
                        message = get_message('Account', 'not availabel')
                        print(message)
                        break
                    
                    if not tem_account_list:
                        break

                    new_account_list = []
                    for account in tem_account_list:
                        no_tranx_account = account.get_obj_no_transaction(date.today())
                        if no_tranx_account:
                            new_account_list.append(account)

                    for account in new_account_list:
                        input_message = get_message(account.name, 'amount')
                        amount = choice_input(input_message)
                        if amount == 0:
                            transaction_file.close()
                            break
                        created = Transaction(date.today(), amount, account.id)

                        transaction_file.set_mode('a')
                        transaction_file.write(created.get_data())
                        account.transaction = created
                        transaction_file.close()
                elif choice == 2:
                    get_view('Category', category_list)
                    input_message = get_message('category', 'select')
                    select_item = choice_input(input_message)
                    if select_item == 0:
                        break
                    # get object to update
                    category = get_obj(select_item, category_list)
                    tem_account_list = category.account
                    if not tem_account_list:
                        message = get_message('Account', 'not availabel')
                        print(message)
                        break
                    
                    if not tem_account_list:
                        break
        # Report
        elif choice == 4:
            new_balance_sheet = init_read()
            while True:
                get_view('Property Type', property_type)
                choice = choice_input(input_message)
                if choice == 0:
                    break
                if choice == 1:
                    assets, assets_amount = new_balance_sheet.assets
                    print(f'Assets Amount: {assets_amount}')
                    for category in assets:
                        print(f'  {category.name}: {category.get_amount(date.today())}')
                        for account in category.account:
                            if account.get_amount(date.today()) == 0:
                                continue
                            print(f'    {account.name}: {account.get_amount(date.today())}')
                    break
                if choice == 2:
                    due, due_amount = new_balance_sheet.due
                    print(f'due Amount: {due_amount}')
                    for category in due:
                        print(f'  {category.name}: {category.get_amount(date.today())}')
                        for account in category.account:
                            if account.get_amount(date.today()) == 0:
                                continue
                            print(f'    {account.name}: {account.get_amount(date.today())}')
                    break
                if choice == 3:
                    liabilities, liabilities_amount = new_balance_sheet.liabilities
                    print(f'liabilities Amount: {liabilities_amount}')
                    for category in liabilities:
                        print(f'  {category.name}: {category.get_amount(date.today())}')
                        for account in category.account:
                            if account.get_amount(date.today()) == 0:
                                continue
                            print(f'    {account.name}: {account.get_amount(date.today())}')
                    break

                
        else:
            message = get_message(msg_type='wrong')
            print(message)


if __name__ == '__main__':
    main()