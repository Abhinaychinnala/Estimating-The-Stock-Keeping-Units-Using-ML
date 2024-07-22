from flask import Flask,render_template,request
import numpy as np
import pickle
import pandas as pd
model=pickle.load(open("model.pkl","rb"))
app=Flask(_name_)
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/y_predict",methods=['POST','GET'])
def y_predict():
    x=[[float(x) for x in request.form.values()]]
    print(x)
    cols=["day_1","day_2","day_3","day_4"]
    print(x)
    pred=model.predict(x)
    print(pred[0])
    return render_template('result.html',prediction_text=pred[0])
if _name_ == "_main_":
   app.run()