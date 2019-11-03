import requests
from flask import Flask, render_template,request
from user import User
app = Flask(__name__)

user = User()

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if not user.is_authenticated:
        if request.method == 'POST':
            form_result = request.form
            username, password = form_result["Username"], form_result["Password"]
            authenticated = user.authenticate(username, password)
            if authenticated:
                return "Succesful Login"
            return "Bad Login"
    return "Already Authenticated"
@app.route('/login')
def login():
    if not user.is_authenticated:
        return render_template("login.html")
    return "Already Authenticated"

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
