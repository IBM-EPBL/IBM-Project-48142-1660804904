#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas
from flask import Flask, request, jsonify, render_template
import pickle
import inputscript

app = Flask(__name__)
model = pickle.load(open('Phishing_Website.pkl','rb'))

@app.route('/')
def home():
    return render_template('welcomepage.html')

@app.route('/website')
def predict():
    return render_template('website.html')

ans = ""   
bns = ""   
@app.route('/result_processing_function', methods=['POST','GET'])
def y_predict():
    url = request.form['url']
    checkprediction = inputscript.main(url)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
     pred="You are safe!!  This is a legitimate Website."
        return render_template('website.html',bns=pred)
    
    else:
        pred="You are on the wrong site. Be cautious!"        
        return render_template('website.html',ans=pred)


@app.route('/predict_api', methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output=prediction[0]
    return jsonify(output)        
 
if __name__ == '__main__':
    app.run()
    



  # In[10]:





# In[ ]:
   