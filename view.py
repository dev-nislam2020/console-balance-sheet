from datetime import date


class ConsoleView:
    def __init__(self, company_name=None, title=None, sub_title=[]):
        self.__date = date.today()
        self.__company_name = company_name
        if company_name != None:
            self.__header_view = f"Today: {self.__date}\n{company_name} BalanceSheet"
        else:
            self.__header_view = f"Today: {self.__date}\nBalanceSheet"
        self.__title = title
        self.__sub_title = sub_title

    @property
    def company_name(self):
        return self.__company_name
    
    @company_name.setter
    def company_name(self, name):
        self.__company_name = name

    @property
    def header_view(self):
        print(self.__header_view)
    
    @header_view.setter
    def header_view(self, name):
        self.__header_view = f"Today: {date}\n{name} BalanceSheet"
    
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def sub_title(self):
        return self.__sub_title

    @sub_title.setter
    def sub_title(self, sub_title):
        self.__sub_title = sub_title
    
    def content_view(self, isTitle=True):
        if isTitle:
            print(f"   {self.title}")
            for i,sub in enumerate(self.sub_title):
                i += 1
                print(f"      {i}: {sub}")
        else:
            for i,sub in enumerate(self.sub_title):
                i += 1
                print(f"   {i}: {sub}")


def get_view(title, sub_title):
    console_view = ConsoleView()
    console_view.header_view
    console_view.title = title
    console_view.sub_title = sub_title
    console_view.content_view()

class MessageView:
    def __init__(self, msg=None, msg_type=None):
        self.__msg = msg
        self.__msg_type = msg_type
        self.__message_content = {
        'create':f'{msg} Create Successful.',
        'update':f'{msg} Update Successful.',
        'delete':f'{msg} delete Successful.',
        'exit':f'{msg} Already exit try again',
        'not found':f'{msg} Not found try again.',
        'not availabel':f'No {msg} Available, Create first',
        'do want':f'Do you want to delete {msg} Item (y/n):',
        'wrong':'You wrong option select, Try again',
        'choice':'Enter Choice & "0" to exit: ',
        'select':f'Select {msg} Item: ',
        'name':f'Enter {msg} Name: ',
        'amount':f'Enter {msg} Amount: '
    }
    @property
    def msg(self):
        return self.__msg
    
    @msg.setter
    def msg(self, msg):
        self.__msg = msg
        self.__message_content = {
        'create':f'{self.__msg} Create Successful.',
        'update':f'{self.__msg} Update Successful.',
        'delete':f'{self.__msg} delete Successful.',
        'exit':f'{self.__msg} Already exit try again',
        'not found':f'{self.__msg} Not found try again.',
        'not availabel':f'No {self.__msg} Available, Create first',
        'do want':f'Do you want to delete {self.__msg} Item (y/n):',
        'wrong':'You wrong option select, Try again',
        'choice':'Enter Choice & "0" to exit: ',
        'select':f'Select {msg} Item: ',
        'name':f'Enter {msg} Name: ',
        'amout':f'Enter {msg} Amount: '
        }
        
    @property
    def msg_type(self):
        return self.__msg_type
    
    @msg_type.setter
    def msg_type(self, msg_type):
        self.__msg_type = msg_type
    
    def message(self):
        return self.__message_content[self.msg_type]

def get_message(msg=None, msg_type=None):
    message_view = MessageView(msg, msg_type)
    return message_view.message()