import sqlite3

class DataManager:
    def __init__(self, db_name="../data/bank.db") -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.initialize_database()
        
    def initialize_database(self):
        self.create_bank_table()
        self.create_client_table()
        self.create_password_table()
        self.create_account_table()
    
    def create_bank_table(self):
        self.execute_sql_command("""
        CREATE TABLE IF NOT EXISTS bank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bank_code TEXT PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)
    
    def create_client_table(self):
        self.execute_sql_command("""
        CREATE TABLE IF NOT EXISTS client (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            tell TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        
    def create_password_table(self):
        self.execute_sql_command("""
        CREATE TABLE IF NOT EXISTS password (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            password TEXT NOT NULL,
            client_id TEXT NOT NULL,
            FOREIGN KEY(client_id) REFERENCES client(id)
        )
        """)
    
    def create_account_table(self):
        self.execute_sql_command("""
        CREATE TABLE IF NOT EXISTS account (
            IBAN TEXT PRIMARY KEY,
            category TEXT NOT NULL,
            balance REAL NOT NULL,
            client_id TEXT NOT NULL,
            FOREIGN KEY(client_id) REFERENCES client(id)
        )
        """)
        
    def insert_bank(self, bank_code, name):
        self.execute_sql_command(f"""
        INSERT INTO bank (bank_code, name)
        VALUES ('{bank_code}', '{name}')
        """)
    
    def insert_client(self, id, name, surname, tell, email, password):
        self.execute_sql_command(f"""
        INSERT INTO client (id, name, surname, tell, email, password)
        VALUES ('{id}', '{name}', '{surname}', '{tell}', '{email}', '{password}')
        """)
    
    def insert_password(self, key, password, client_id):
        self.execute_sql_command(f"""
        INSERT INTO password (key, password, client_id)
        VALUES ('{key}', '{password}', '{client_id}')
        """)
    
    def insert_account(self, IBAN, category, balance, client_id):
        self.execute_sql_command(f"""
        INSERT INTO account (IBAN, category, balance, client_id)
        VALUES ('{IBAN}', '{category}', {balance}, '{client_id}')
        """)
        
    def select_bank(self, bank_code):
        self.cursor.execute(f"""
        SELECT * FROM bank WHERE bank_code = '{bank_code}'
        """)
        return self.cursor.fetchone()
    
    def select_client(self, id):
        self.cursor.execute(f"""
        SELECT * FROM client WHERE id = '{id}'
        """)
        return self.cursor.fetchone()
    
    def select_password(self, key):
        self.cursor.execute(f"""
        SELECT * FROM password WHERE key = '{key}'
        """)
        return self.cursor.fetchone()
    
    def select_account(self, IBAN):
        self.cursor.execute(f"""
        SELECT * FROM account WHERE IBAN = '{IBAN}'
        """)
        return self.cursor.fetchone()
        
    def close(self):
        self.conn.close()
    
    def execute_sql_command(self, sql_command):
        try:
            self.cursor.execute(sql_command)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
