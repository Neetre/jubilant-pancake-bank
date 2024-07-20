'''


Neetre 2024
'''

import random
import string


PATTERN_IBAN = r"^[A-Z]{2}\d{2}[A-Z\d]{11,30}$"


def generate_iban(country_code: str):
    check_digits = str(random.randint(10, 99))
    bban_length = random.randint(11, 30)
    bban = ''.join(random.choices(string.ascii_uppercase + string.digits, k=bban_length))
    iban = country_code + check_digits + bban
    return iban


class Account:
    def __init__(self, id_client: str, money: float, country: str):
        self.__IBAN = generate_iban(country)
        self.__id_client = id_client
        self.__money = money
        
    @property
    def IBAN(self):
        return self.__IBAN
    
    @property
    def money(self):
        return self.__money
    
    @property
    def id_client(self):
        return self.__id_client
    
    def deposit(self, amount: float):
        self.__money += amount
        
    def withdraw(self, amount: float):
        if amount <= 0:
            return False
        if self.__money < amount:
            return False
        
        self.__money -= amount
        return True
    
    def __str__(self) -> str:
        return f"Account: {self.__IBAN} - Money: {self.__money}"
    

class AccountCC(Account):
    def __init__(self, id_client: str, money: float, trans_cost=2.0, n_trans_free=3, country=""):
        super().__init__(id_client, money, country)
        self.__trans_cost = trans_cost
        self.__n_trans_free = n_trans_free
        self.__n_trans = 0
        
    def deposit(self, amount: float):
        self.__n_trans += 1
        super().deposit(amount)
    
    def withdraw(self, amount: float):
        self.__n_trans += 1
        super().withdraw(amount)
        
    def ded_comm(self):
        if self.__n_trans > self.__n_trans_free:
            self.deposit(-((self.__n_trans - self.__n_trans_free) * self.__trans_cost))
            self.__n_trans = 0

class AccountCD(Account):
    rate_def = 3
    
    def __init__(self, id_client: str, money: float, rate: int):
        super().__init__(id_client, money)
        self.__account_rate = rate if rate != 0 else AccountCD.rate_def
        
    def add_inter(self):
        self.deposit(self.__money * (self.__account_rate / 100))
        

class AccountCDV(AccountCD):
    def __init__(self, id_client: str, money: float, rate: int, n_months: int):
        super().__init__(id_client, money, rate)
        self.__n_months = n_months
        self.__penalty = 20.0
        
    def add_inter(self):
        self.__n_months -= 1
        super().add_inter()

    def withdraw(self, amount: float):
        if self.__n_months <= 0:
            return super().withdraw(amount)
        else:
            if self.__money < amount + self.__penalty:
                raise ValueError("Not enough money for withdrawal")
            self.deposit(-self.__penalty)
            return super().withdraw(amount)
        
        
class CryptoWallet(Account):
    def __init__(self, id_client: str, money: float, crypto_type: str, key_pair: tuple):
        super().__init__(id_client, money)
        self.__crypto_type = crypto_type
        self.__key_pair = key_pair
        
    @property
    def crypto_type(self):
        return self.__crypto_type
    
    @property
    def public_key(self):
        return self.__key_pair[1]
    
    def get_balance(self):
        return self.money
    
    def send_transaction():
        pass
    
    def receive_transaction():
        pass
    
    def __str__(self) -> str:
        return f"CryptoWallet: {self.IBAN} - Type: {self.__crypto_type} - Balance: {self.money}"
