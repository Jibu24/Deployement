json_data = {'Gender': 'Male',
             'Married': 'No',
             'Dependents': '0',
             'Education': 'Graduate',
             'Self_Employed': 'No',
             'ApplicantIncome': 5849,
             'CoapplicantIncome': 0.0,
             'LoanAmount': 360.0,
             'Loan_Amount_Term': 360.0,
             'Credit_History': 1.0,
             'Property_Area': 'Urban'}

import requests
URL = "http://192.168.0.19:5000/scoring" #base url local host
URL_cloud = "http://ec2-3-135-215-11.us-east-2.compute.amazonaws.com:5000/scoring" 

r=requests.post(url = URL_cloud, json = json_data)

print(r.json())