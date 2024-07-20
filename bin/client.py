
class Client:
    def __init__(self, id, name, surname, tell, email, password) -> None:
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__tell = tell
        self.__email = email
        self.__password = password
        
        self.bank_accounts = []