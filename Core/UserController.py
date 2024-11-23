import hashlib,os,json

SUPERMANAGER = "spmngr"
USER = "usr"

def check(username:str, password:str):
    """
    User info checker
    """
    
    # Initialize a sha1 object
    sha1 = hashlib.sha1()

    # Find username
    if not os.path.exists(f"./Core/Users/{username}.json"):
        return False

    # If have, then check sha1
    user = json.load(open(f"./Core/Users/{username}.json"))

    # Check password
    sha1.update(password.encode('utf-8'))
    if sha1.hexdigest() == user["password"]:
        return True
    else:
        return False
    
    return "BUG BUG BUG BUG BUG"

def register(username:str, password:str, permission:str):
    """
    Create a new user

    :param username: The username of the user
    :param password: The password of the user
    :param permission: The permission of the user, please use "SUPERMANAGER" or "USER"
    """

    # Initialize a sha1 object and calc password's sha1
    sha1 = hashlib.sha1()
    sha1.update(password.encode('utf-8'))
    sha1_password = sha1.hexdigest()

    # Check if user already exists
    if os.path.exists(f"./Core/Users/{username}.json"):
        return False

    # Create a new user
    user = {
        "username":username,
        "password":sha1_password,
        "permission":permission
    }

    # Write
    json.dump(user, open(f"./Core/Users/{username}.json","w"), indent=4)

    return True

def delete(username:str):
    """
    Delete a user
    """

    if not os.path.exists(f"./Core/Users/{username}.json"):
        return False
    
    os.remove(f"./Core/Users/{username}.json")
    return True

def have(username:str):
    return os.path.exists("./Core/Users/"+username+".json")

def getpermission(username: str):
    try:
        user = json.load(open("./Core/Users/"+username+".json", "r"))
    except: return "usr"
    return user ["permission"]