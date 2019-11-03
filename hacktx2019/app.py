from flask import Flask, request, render_template
from ocr import recognize_printed_text
from util import allowed_file
from werkzeug.utils import secure_filename
import re
from user import User

WORDS_TO_IGNORE = ['minutes', 'seconds', 'hours', 'degrees', 'f', 'c', 'inches', 'feet', 'centimeters', 'millimeters', 'to']
regex = re.compile('[\s,.\?!]')


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

@app.route('/rec', methods=['POST'])
def rec():
	if request.method == 'POST':
		if 'proportion' not in request.form:
			return redirect(request.url)
		proportion = 1
		try:
			proportion = float(request.form['proportion'])
		except ValueError:
			return redirect(request.url)
			
		
			
	
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			lines = recognize_printed_text("a433d6de318d4cf783be944b527f85d4", file.stream)
			print(lines)
			output = []
			for line in lines:
				words = regex.split(line)
				for x in range(0, len(words)):
					try:
						curr_word = words[x]
						number = None
						if '/' in curr_word:
							temp = curr_word.split('/')
							if len(temp) == 2:
								try:
									numer = int(temp[0]) * proportion
									denom = int(temp[1])
									number = numer/denom
									output.append(number)
								except:
									pass
						elif '-' in curr_word:
							temp = curr_word.split('-')
							if len(temp) == 2:
								try:
									numer = int(temp[0])
									denom = int(temp[1])
									output.append(str(numer) + '-' + str(denom))
								except:
									pass
						else:
							number = float(words[x])
							if number < 100 and (x >= len(words) - 1 or words[x + 1] not in WORDS_TO_IGNORE):
								number *= proportion
							output.append(number)
					except ValueError:
						output.append(curr_word)
			return str(output)
						
					
							
					
						
			
			
	return "Hellow Rec!"

@app.route('/find')
def find():
	return "Hello Find!"

@app.route('/')
def hello_world():
	return '''
	<!doctype html>
	<title>Doublr</title>
	<h1>Double, halve, or make any other portions with your recipe!</h1>
	<form action="/rec" method=post enctype=multipart/form-data>
		<input type=text name=proportion>
		<input type=file name="file">
		<input type=submit value=Submit>
	</form>
	'''

if __name__ == '__main__':
	app.run(debug=True)
