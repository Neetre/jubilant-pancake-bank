
import re
from client import Client\

class Bank:
    def __init__(self, name, bank_code) -> None:
        self.__name = name
        self.__bank_code = bank_code
        self.__clients = []
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def set_name(self, new_name):
        self.__name = new_name
    
    @property
    def bank_code(self) -> str:
        return self.__bank_code
    
    @bank_code.setter
    def set_bank_code(self, new_code):
        self.__bank_code = new_code
        
    def new_client(self, id, name, surname, tell, email, password):
        for client in self.__clients:
            if client.id == id:
                print("Client already exist")
                return
        
        new_client = Client(id, name, surname, tell, email, password)
        self.__clients.append(new_client)
        
    def calculate_monthly_interest(self):
        for client in self.__clients:
            for account in client.bank_accounts:
                if isinstance(account, ):
                    account.add_inter()
                if isinstance(account, ):
                    account.add_inter()
                    
    def overall_bank_balance(self):
        tot = 0
        for client in self.__clients:
            tot += client.get_tot_money
        return tot