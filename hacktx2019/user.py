import pymongo

client = pymongo.MongoClient("mongodb+srv://hacktx-user:hacktx-user@hacktx-mb5vn.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client["HackTxDatabase"]
users = db["Users"]

class User():
    def __init__(self):
        self.is_authenticated = False

    def authenticate(self, username, password):
        self.is_authenticated = False
        for user in users.find():
            if user['username'] == username:
                if password == user['password']:
                    self.is_authenticated = True
        return self.is_authenticated
