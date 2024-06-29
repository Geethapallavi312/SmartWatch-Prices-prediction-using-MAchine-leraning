import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
model1= pickle.load(open('SW.pkl','rb'))
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict')
def index():
    return render_template('predict.html')
@app.route('/data_predict',methods=['GET','POST'])
def predict():
    brand=request.form['Brand']
    if brand == 'Garmin':
        brand = 8
    if brand == 'Mobvoi':
        brand = 18
    if brand == 'Fitbit':
        brand = 6
    if brand == 'Fossil':
        brand = 7
    if brand == 'Amazfit':
        brand = 0
    if brand == 'Samsung':
        brand = 30
    if brand == 'Huawei':
        brand = 10

    model = request.form['Model']

    if model == 'Hybrid HR':
        model = 44
    if model == 'Venu Sq':
        model = 106
    if model == 'MagiWatch 2':
        model= 56
    if model == 'TicWatch Pro 3':
        model= 97
    if model == 'Vapor x':
        model= 104
    if model == 'Z':
        model = 132
    
    os= request.form['Operating System']

    if os == 'Wear Os':
        os=  31
    if os == 'Garmin OS':
        os = 9
    if os == 'Lite OS':
        os= 12

    connect = request.form['connectivity']

    if connect == 'Bluetooth, Wi-Fi':
        connect = 1
    if connect == 'Bluetooth, Wi-Fi, Cellular':
        connect = 2
    if connect == 'Bluetooth':
        connect = 0
    if connect == 'Bluetooth, Wi-Fi, GPS':
        connect = 3
    if connect == 'Bluetooth,Wi-Fi, NFC':
        connect = 4

    display_type = request.form['Display Type']

    if display_type == 'AMOLED':
        display_time = 0
    if display_type == 'LCD':
        display_type = 9

prediction = model1.predict(pd.DataFrame([[brand,model,os,connect,display_type,display_size,resolution,water,battery, gps, nfc]],
                              columns=['Brand','Model','Operating System','Connectivity','Display Type','Display Size','Resolution','Water Resistance','Battery Life','GPS','NFC']))
prediction = np.round(prediction,2)

return  render_template('watch_prediction.html',prediction_text = "is {}".format(prediction))

if __name__ == ' __main__':
    app.run()                             