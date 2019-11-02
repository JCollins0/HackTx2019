from flask import Flask
app = Flask(__name__)
import pymongo

@app.route('/')
def hello_world():

    client = pymongo.MongoClient("mongodb+srv://hacktx-user:hacktx-user@hacktx-mb5vn.azure.mongodb.net/test?retryWrites=true&w=majority")
    print(client.list_database_names())

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
