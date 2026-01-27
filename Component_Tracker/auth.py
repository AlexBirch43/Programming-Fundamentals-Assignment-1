#  Hardcoded credentials
Users = {
    "ENGINEER": "ENGINEER",
    "MANAGER": "MANAGER"
}
def validate_user(username, password):
    return username in Users and Users[username] == password

def get_role(username):
    if username == "ENGINEER":
        return "ENGINEER"
    return "MANAGER"
