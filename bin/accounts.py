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
    def __init__(self, id_client: str, money: float):
        self.__IBAN = generate_iban()
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