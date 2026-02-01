#  Hardcoded credentials
Users = {
    "ENGINEER": "ENGINEER",
    "MANAGER": "MANAGER"
}
def validate_user(username, password):
    username_upper = username.upper()                                       #allows username not to be case-sensitive
    return username_upper in Users and Users[username_upper] == password

def get_role(username):
    username = username.upper()                                             #allows username not to be case-sensitive
    if username == "ENGINEER":
        return "ENGINEER"
    return "MANAGER"
