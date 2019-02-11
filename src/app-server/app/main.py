from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/transact', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        amount = request.form['amount']
        from_address = request.form['from']
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return "Bad request " + error
