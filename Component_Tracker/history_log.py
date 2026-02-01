from datetime import datetime                                      #imports tool to provide current date/time

LOG_FILE = "history.log"

def log_action(user, action):                                     #function takes user role and the action undertaken
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")      #takes current date/time and formats into readable string
    with open(LOG_FILE, "a") as log:                              # "a" means append, rather than overwrite, every new action is added to the end of the file
        log.write(f"[{timestamp}] {user}: {action}\n")
