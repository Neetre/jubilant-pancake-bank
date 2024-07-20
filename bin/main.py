from bank import Bank
from log import Log
import os
from data_manager import DataManager
from accounts import *

def main(logger: Log):
    
    bank = Bank("Testing Bank", "BP001")
    
    bank.new_client("C1", "Mario", "Rossi", "1234567890", "test@gmail.com", "pizza_red")

    for client in bank.clients:
        if client.name == "Mario":
            client.new_account(AccountCC("C1", 2000.0))
            
    bank.calculate_monthly_interest()
    print(f"The bank has: {bank.overall_bank_balance()}")
    
    for category in ["CC", "CD", "CDV"]:
        
        print(f"Money of category {category}: {bank.overall_category_balance(category)}")
        
if __name__ == "__main__":
    name_f = os.path.basename(__file__)
    logger = Log(name_f)
    logger.log(False)
    main(logger)
    logger.log(True)