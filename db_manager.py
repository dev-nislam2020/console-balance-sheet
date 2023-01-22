import csv, os
from models import BalanceSheet, Category, Account, Transaction
from validation import get_obj, get_obj_list, property_type, set_property_type


class CsvFileReadWrite:
    '''using this class for csv file reading and writing'''
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        if self.mode == 'r':
            self.fp = open(self.filename, self.mode, encoding='utf8')
            self.reader = csv.reader(self.fp, delimiter=',')
        else:
            self.fp = open(self.filename, self.mode, encoding='utf8')
            self.writer = csv.writer(self.fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

    def set_filename(self, name):
        self.filename = name

    def set_mode(self, mode):
        self.mode = mode
        if self.mode == 'r':
            self.fp = open(self.filename, self.mode, encoding='utf8')
            self.reader = csv.reader(self.fp, delimiter=',')
        elif self.mode == 'a':
            self.fp = open(self.filename, self.mode, encoding='utf8')
            self.writer = csv.writer(self.fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
        else:
            self.fp = open(self.filename, self.mode, encoding='utf8')
            self.writer = csv.writer(self.fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

    def close(self):
        self.fp.close()

    def write(self, elems):
        self.writer.writerow(elems)
    
    def read(self):
        if self.reader:
            return self.reader

    def size(self):
        return os.path.getsize(self.filename)

    def fname(self):
        return self.filename

init_file = {
    'file name':['category','account','transaction'],
    'table name':[
        ['sn','name','pro_type'],
        ['sn','name','category_id'],
        ['sn','date','amount','account_id']
    ]
}

def get_reader(f_name):
    csv_file = CsvFileReadWrite(f"./db/{f_name}.csv", 'r')
    return csv_file.read()

def init_write():
    for i,f_name in enumerate(init_file['file name']):
        in_file = CsvFileReadWrite(f'./db/{f_name}.csv', 'r')
        if in_file.size() == 0:
            in_file.set_mode('w')
            elems = init_file['table name'][i]
            in_file.write(elems)


def init_read():
    balance_sheet = BalanceSheet()
    # reading category file
    category_reader = get_reader(init_file['file name'][0])
    account_reader = get_reader(init_file['file name'][1])
    transaction_reader = get_reader(init_file['file name'][2])
    
    for i,category in enumerate(category_reader):
        if i == 0:
            continue
        sn, name, pro_type = category
        created = Category(name, pro_type)
        created.id = int(sn)
        select_item = property_type.index(pro_type)
        select_item = select_item + 1
        set_property_type(balance_sheet, select_item, created)
    # reading account file
    
    category_list = balance_sheet.get_list()
    for i,account in enumerate(account_reader):
        if i == 0:
            continue
        sn, name, category_id = account
        created = Account(name, int(category_id))
        created.id = int(sn)
        obj = get_obj(int(category_id), category_list)
        obj.account = created

    # readng transaction
    account_list = get_obj_list(category_list)
    for i,transaction in enumerate(transaction_reader):
        if i == 0:
            continue
        sn, date, amount, account_id = transaction
        created = Transaction(date, int(amount), int(account_id))
        created.id = int(sn)
        obj = get_obj(int(account_id), account_list)
        obj.transaction = created
    
    return balance_sheet