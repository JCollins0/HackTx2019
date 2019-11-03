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
    return "Hello Find!"

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
