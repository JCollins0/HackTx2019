from flask import Flask
app = Flask(__name__)


@app.route('/login')
def login():

    import pymongo
    client = pymongo.MongoClient("mongodb+srv://hacktx-user:hacktx-user@hacktx-mb5vn.azure.mongodb.net/test?retryWrites=true&w=majority")
    print(client.list_database_names())

    return "Hello Login!"

@app.route('/rec')
def rec():
    return "Hellow Rec!"

@app.route('/find')
def find():
    return "Hello Find!"

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
