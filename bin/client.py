'''
Neetre 2024
'''

from security import Security

PATTERN_IBAN = r"^[A-Z]{2}\d{2}[A-Z\d]{11,30}$"

class Client:
    def __init__(self, id, name, surname, tell, email, password, country) -> None:
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__tell = tell
        self.__email = email
        self.__country = country
        self.__password = Security.generate(password)
        self.__active = True

        self.__bank_accounts = []
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname
    
    @property
    def tell(self):
        return self.__tell
    
    @tell.setter
    def tell(self, new_tell):
        self.__tell = new_tell
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        self.__email = new_email
        
    @property
    def country(self):
        return self.__country
    
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, new_password):
        self.__password = new_password
    
    @property
    def active(self) -> bool:
        return self.__active
    
    @active.setter
    def active(self, new_status: bool):
        self.__active = new_status
        
    @property
    def bank_accounts(self) -> list:
        return self.__bank_accounts
    
    def len_accounts(self) -> int:
        return len(self.__bank_accounts)
    
    def new_account(self, account: object):
        self.__bank_accounts.append(account)
        
    def close_account(self, IBAN: str):
        for account in self.__bank_accounts:
            if account.IBAN == IBAN and account.money > 0:
                self.__bank_accounts.remove(account)
                return account.money
        return 0
    
    def get_tot_money(self) -> float:
        return sum(account.money for account in self.__bank_accounts)
    
    def __str__(self):
        return f"Client: {self.__name} {self.surname} - ID: {self.__id}"
