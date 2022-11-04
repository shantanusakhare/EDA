import os
from deta import Deta
from dotenv import load_dotenv

#Load the environment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

#Initialize with a project Key
deta = Deta(DETA_KEY)

# this is how to create/connect a db

db = deta.Base("user_db")

def insert_user(username, name, password):
    """ Return the user on a successful user creation, other wise raises and error"""
    return db.put({"key": username, "name": name, "password": password})

insert_user("npoojari", "Nikhil Poojari", "123456")

def fetch_all_users():
    """Return a dict of all users"""
    res= db.fetch()
    return res.items

def get_user(username):
    """If not found, the function will return none"""
    return db.get(username)

def update_user(username, updates):
    """If the item is updated , returns none. Otherwize, an exception is rased"""
    return db.update(updates, username)

def delete_user(username):
    """Always returns None, Even if the key does not exist"""
    return db.delete(username)

# delete_user("npoojari")