from security import Security

PATTERN_IBAN = r"^[A-Z]{2}\d{2}[A-Z\d]{11,30}$"

class Client:
    def __init__(self, id, name, surname, tell, email, password) -> None:
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__tell = tell
        self.__email = email
        self.__password = password
        self.__key_pair = Security.generate_key_pair(password)
        
        self.__active = True

        self.__bank_accounts = []
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def tell(self):
        return self.__tell
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self) -> str:
        return self.__password
    
    @property
    def active(self) -> bool:
        return self.__active
    
    @active.setter
    def active(self, new_status):
        self.__active = new_status
        
    @property
    def bank_accounts(self) -> list:
        return self.__bank_accounts
    
    def len_accounts(self) -> int:
        return len(self.__bank_accounts)
    
    def new_account(self, account):
        self.__bank_accounts.append(account)
        
    def close_account(self, category):
        for account in self.__bank_accounts:
            if account.__class__.__name__ == category and account.money > 0:
                self.__bank_accounts.remove(account)
                return account.money
        return 0
    
    def get_tot_money(self) -> float:
        return sum(account.money for account in self.__bank_accounts)
    
    def __str__(self):
        return f"Client: {self.__name} {self.surname} - ID: {self.__id}"