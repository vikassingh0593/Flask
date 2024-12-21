from flask import Flask

# master variable - controls entire application
app = Flask(__name__)

# API endpoints
@app.route('/')
def home():
    return "<h1>Loan Approval Application V2!!!</h1>"


@app.route('/ping')
def ping():
    return {"message":"Hey there..."}