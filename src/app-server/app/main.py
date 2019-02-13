from flask import Flask
from kafka_consumer import kafka_consumer_gen
import requests
from flask import json
from flask import make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/consume')
def consume():
    consumer = kafka_consumer_gen()
    value_array = []
    for _ in range(10):
        value_array.append(next(consumer))
    response = json.dumps(value_array)
    return response




@app.route('/transact', methods=['POST', 'GET'])
def transact():
    error = None
    if request.method == 'POST':
        amount = request.form['amount']
        from_address = request.form['from']
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return "Bad request " + error



@app.route('/api')
def polling_api():
    """
    Need to implement discover if we want this, too dynamic otherwise.
    """
    endpoint = "http://localhost:4040/api/v1"
    running_app_id = get_running_application()
    if(running_app_id == -1):
        return "No streaming job running!"
    running_app_id= "app-20190211174759-0005"
    data_postfix = "/applications/" + running_app_id + "/streaming/statistics"
    json_response = requests.get(endpoint + data_postfix).json()
    return json_response



def get_running_application():
    return 0
    return app_id



def parse_application_data(data):
    return -1
    return app_id
