
from crypt import methods
from ssl import SSLSyscallError
from typing import final
import joblib
from flask import flask, render_template, request 
import preprocess
import numpy as np

app = flask(__name__)

scaler = joblib.load('Models/scaler.h5')
model =  joblib.load('Models/model.h5')

@app.route('/')
def index ()  :
    return render_template('index.html')

@app.route('/oredict', methods=['POST','GET'])
def get_prediction():

    if request.method=='POST':
         CREDIT_SCORE = request.form['score']
        VEHICLE_OWNERSHIP = request.form ['ownership']
        ANNUAL_MILEAGE = request.form ['mileage']
        SPEEDING_VIOLATIONS = request.form ['violations']
        PAST_ACCIDENTS = request.form ['accidents']
        AGE = request.form ['AGE']
        DRIVING_EXPERIENCE = request.form['DRIVING_EXPERIENCE']
        EDUCATION =  request.form['EDUCATION']
        INCOME = request.form ['INCOME']
    data = {'score': score ,'ownership': owner , 'mileage' mileage : , 'violations' violations : , 'accidents' : accidents ,
     'AGE' : age , 'DRIVING_EXPERIENCE' : experience , 'EDUCATION' : education , 'INCOME' : income }

     final_data = preprocess.preprocess_data(data)
     scaled_data = scaler.transform([final_data])
     prediction = model.predict()[0] 


    return render_template ('prediction.html', insurance_availability = str(prediction))


    if __name__=='__main__' :
        app.run (debug=True)