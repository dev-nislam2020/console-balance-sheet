from datetime import date


# models class
class BalanceSheet:
    __id = 0
    def __init__(self, current_date=date.today()):
        type(self).__id += 1
        self.__sn = type(self).__id
        self.__date = current_date
        self.__assets = []
        self.__due = []
        self.__liabilities = []
        self.__balance = {
            'assets amount':0,
            'due amount':0,
            'liabilities amount':0
        }
    
    @property
    def id(self):
        return self.__sn

    @id.setter
    def set_id(self, id):
        self.id = id
    
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def assets(self):
        if self.__assets:
            amount = 0
            for category in self.__assets:
                amount = amount + category.get_amount(self.__date)
            self.__balance['assets amount'] = amount
        return (self.__assets, amount)

    @assets.setter
    def assets(self, category):
        self.__assets.append(category)
        
    @property
    def due(self):
        if self.__due:
            amount = 0
            for category in self.__due:
                 amount = amount + category.get_amount(str(self.__date))
            self.__balance['assets amount'] = amount
        return (self.__due, amount)

    @due.setter
    def due(self, category):
        self.__due.append(category)

    @property
    def liabilities(self):
        if self.__liabilities:
            amount = 0
            for category in self.__liabilities:
                 amount = amount + category.get_amount(self.__date)
            self.__balance['liabilities amount'] = amount
        return (self.__liabilities, amount)
    
    @liabilities.setter
    def liabilities(self, category):
        self.__liabilities.append(category)

    def get_balance(self):
        return self.__balance
    
    def get_data(self):
        '''its gives you class data list'''
        data = []
        data.append(self.__sn)
        data.append(self.__date)
        data.append(self.__balance['assets amount'])
        data.append(self.__balance['due amount'])
        data.append(self.__balance['liabilities amount'])
        data.append(self.__balance['assets amount'] + self.__balance['total due'] - self.total_balance['total liabilities'])
        return data
    
    def get_list(self):
        return [*self.__assets, *self.__due, *self.__liabilities]

    def __str__(self):
        return f"Id: {self.__sn}, Date: {self.__date}\
             Total Assets: {self.__balance['assets amount']}\
             Total due: {self.__balance['due amount']}\
             Total liabilities: {self.__balance['liabilities amount']}\
             Total Balance: {self.__balance['assets amount'] + self.__balance['total due'] - self.total_balance['total liabilities']}"

class Category:
    __id = 0
    def __init__(self, name=None, property_type=None):
        type(self).__id += 1
        self.__sn = type(self).__id
        self.__name = name
        self.__property_type = property_type
        self.__account = []

    @property
    def id(self):
        return self.__sn

    @id.setter
    def id(self, id):
        self.__sn = id
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def property_type(self):
        return self.__property_type
    
    @property_type.setter
    def property_type(self, property_type):
        self.__property_type = property_type
    
    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, account):
        self.__account.append(account)
    
    def get_amount(self, current_date):
        if self.__account:
            total_amount = 0
            for current_account in self.__account:
                total_amount = total_amount + current_account.get_amount(str(current_date))
            return total_amount

    def get_data(self):
        '''its gives you class data list'''
        data = []
        data.append(self.__sn)
        data.append(self.__name)
        data.append(self.__property_type)
        return data
    
    def __str__(self):
        return f'{self.__name}'

class Account:
    __id = 0
    def __init__(self, name=None, category_id=None):
        type(self).__id += 1
        self.__sn = type(self).__id
        self.__name = name
        self.__category_id = category_id
        self.__transaction = []
    
    @property
    def id(self):
        return self.__sn

    @id.setter
    def id(self, id):
        self.__sn = id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def category_id(self):
        return self.__category_id

    @category_id.setter
    def category_id(self, id):
        self.__category_id = id
    
    @property
    def transaction(self):
        return self.__transaction

    @transaction.setter
    def transaction(self, transaction):
        self.__transaction.append(transaction)
    
    def get_amount(self, current_date):
        if self.__transaction:
            for trans in self.__transaction:
                if str(current_date) == trans.transaction_date:
                    return trans.amount
        return 0
    
    def get_obj_no_transaction(self, current_date):
        if not self.__transaction:
            return True
        for trans in self.__transaction:
            if str(current_date) == trans.transaction_date:
                return False
        return True

    def get_data(self):
        '''its gives you class data list'''
        data = []
        data.append(self.__sn)
        data.append(self.__name)
        data.append(self.__category_id)
        return data
    
    def __str__(self):
        return f'{self.__name}'

class Transaction:
    __id = 0
    def __init__(self, date, amount=0, account_id=0):
        type(self).__id += 1
        self.__sn = type(self).__id
        self.__transaction_date = date
        self.__amount = amount
        self.__account_id = account_id

    @property
    def id(self):
        return self.__sn
    
    @id.setter
    def id(self, id):
        self.__sn = id
    
    @property
    def transaction_date(self):
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, data):
        self.__transaction_date = date
    
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def account_id(self, id):
        self.__account_id = id
    
    @account_id.setter
    def account_id(self):
        return self.__account_id

    def get_data(self):
        '''its gives you class data list'''
        data = []
        data.append(self.__sn)
        data.append(self.__transaction_date)
        data.append(self.__amount)
        data.append(self.__account_id)
        return data
    
    def __str__(self):
        return f'id: {self.__sn} Date: {self.__transaction_date,} Amount: {self.__amount}'
