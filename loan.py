from flask import Flask, request
import pickle


# master variable - controls entire application
app = Flask(__name__)

# model loading
model_file = open("classifier.pkl", "rb")
model = pickle.load(model_file)

# API endpoints
@app.route('/')
def home():
    return "<h1>Loan Approval Application V2!!!</h1>"


@app.route('/ping')
def ping():
    return {"message":"Hey there...H"}

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'GET':        
        return "I will make the predictions."
    else:
        # post request along with the data
        # then i will make the prediction.
        loan_req = request.get_json()
        
        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1
        
        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History= loan_req['Credit_History']           

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        result = model.predict([input_data])
        
        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"


        return {"loan_approval_status":pred}

@app.route('/carprice')
def pinga():
    return {"message":"This will predict the resale price of the car. "}