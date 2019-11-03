from flask import Flask
import requests
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
    response = requests.get("https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,%20flour,%20sugar&number=2&apiKey=954c30079df04c4fafe027b25a77ff5d")
    print(response)
    return "Hello Find!"

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
