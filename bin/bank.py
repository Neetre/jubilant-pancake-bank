'''


Neetre 2024
'''

import re
from client import Client
from accounts import *

class Bank:
    def __init__(self, name: str, bank_code: str) -> None:
        self.__name = name
        self.__bank_code = bank_code
        self.__clients = []
        self.__country = bank_code[:2]
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def set_name(self, new_name: str):
        self.__name = new_name
    
    @property
    def bank_code(self) -> str:
        return self.__bank_code
    
    @property
    def clients(self):
        return self.__clients
    
    @bank_code.setter
    def set_bank_code(self, new_code: str):
        self.__bank_code = new_code
        
    @property
    def country(self) -> str:
        return self.__country
        
    def new_client(self, id: str, name: str, surname: str, tell: str, email: str, password: str, country: str):
        for client in self.__clients:
            if client.id == id:
                print("Client already exist")
                return
        
        new_client = Client(id, name, surname, tell, email, password, country)
        self.__clients.append(new_client)
        
    def calculate_monthly_interest(self):
        for client in self.__clients:
            for account in client.bank_accounts:
                if isinstance(account, AccountCD):
                    account.add_inter()
                if isinstance(account, AccountCDV):
                    account.add_inter()
                    
    def overall_bank_balance(self):
        tot_bank = 0
        for client in self.__clients:
            tot_bank += client.get_tot_money()
        return tot_bank
    
    def overall_category_balance(self, category: str):
        tot_category = 0
        for client in self.__clients:
            for account in client.bank_accounts:
                if category == "CC" and isinstance(account, AccountCC):
                    tot_category += account.money
                elif category == "CD" and isinstance(account, AccountCD):
                    tot_category += account.money
                elif category == "CDV" and isinstance(account, AccountCDV):
                    tot_category += account.money
        return tot_category
    
    def __str__(self) -> str:
        return f"Bank: {self.__name} - Code: {self.__bank_code}"
