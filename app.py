# Import dependencies
from flask import Flask
# Create Flask instance
app = Flask(__name__)
# Create first route (root)
@app.route('/')
def hello_world():
    return 'Hello world'
# creat second route (skill drill)    
@app.route('/welcome')
def welcome():
    return 'Welcome to Flask'
