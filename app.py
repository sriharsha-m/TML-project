#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask,render_template,request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
model=pickle.load(open('model_p','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('tmlpy.html')
standard_to=StandardScaler()
@app.route("/predict",methods=["POST"])
def predict():
    if request.method=='POST' :
        rl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        SubD=request.form['division']
        if SubD=='ANDAMAN & NICOBAR ISLANDS' :
            rl[0]=1
        if SubD=='ARUNACHAL PRADESH' :
            rl[1]=1
        m1=int(request.form['m1'])
        m2=int(request.form['m2'])
        m3=int(request.form['m3'])
        l1=[]
        l2=[m1,m2,m3]+rl
        m11=m1**2
        m22=m2**2
        m33=m3**2
        mm=m1*m2*m3
        avg1=(m1+m2+m3)**2
        avg2=(m1+m2)**2+(m2+m3)**2+(m1+m3)**2
        l3=[m11,m22,m33,mm,avg1,avg2]
        l2=l2+l3
        l1.append(l2)
        ex=np.array(l1)
        prediction=model.predict(ex)
        output=round(prediction[0],2)
        if output<0 :
            return render_template('tmlpy.html',prediction_texts="Sorry")
        else :
            return render_template('tmlpy.html',prediction_text="Rain fall for predicted month is {}".format(output))
    else :
        return render_template('tmlpy.html')
if __name__=="__main__" :
    app.run(debug=True)
        


# In[ ]:




