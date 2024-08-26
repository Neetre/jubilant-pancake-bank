import platform
import os.path
from datetime import datetime
from icecream import ic


ic.disable()


class Log:
    def __init__(self, name_f: str, f_log="../log/trace.log"):
        self.name_f = name_f
        self.f_log = f_log
    
    def log(self, term: bool):
        try:
            with open(self.f_log, "a") as flog:
                current_time = datetime.now().strftime("%H:%M:%S del giorno %m/%d/%Y")
                uname = platform.uname()

                if term is False:
                    log_message = f"Program started at {current_time}"
                    log_entry = (
                    "----------------------------------------------\n"
                    f"{current_time}, {uname.node}, {uname.system}, {self.name_f}, {log_message}\n"
                )
                else:
                    log_message = f"Program terminated at {current_time}"
                    log_entry = (
                    f"{current_time}, {uname.node}, {uname.system}, {self.name_f}, {log_message}\n"
                )

                flog.write(log_entry)
        except Exception as ex:
            self.write_error(ex)
            
    def write_error(self, error: str):
        current_time = datetime.now().strftime("%H:%M:%S del giorno %m/%d/%Y")
        with open(self.f_log, 'a') as file:
            file.write(f"File: {self.name_f}, Error: {error}, Time: {current_time}\n")
            
    def write_msg(self, msg):
        current_time = datetime.now().strftime("%H:%M:%S del giorno %m/%d/%Y")
        with open(self.f_log, 'a') as file:
            file.write(f"File: {self.name_f}, Message: {msg}, Time: {current_time}\n")


if __name__ == "__main__":
    name_f = os.path.basename(__file__)
    logger = Log(name_f)
    logger.log(False)
    # Execution
    logger.log(True)
