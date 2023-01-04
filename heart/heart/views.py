from django.shortcuts import render
from django.http import HttpResponse
from heart_data.models import Heart_data
import joblib
import pandas as pd
import numpy as np
def heart_info(request):
    return render(request,'index.html')
def heart_check(request):
    name = request.GET['name1']
    age = float(request.GET['age'])
    sex = float(request.GET['sex'])
    cp = float(request.GET['cp'])
    bps = float(request.GET['bps'])
    chol = float(request.GET['chol'])
    thalach = float(request.GET['thalach']) 
    oldpeak = float(request.GET['oldpeak'])
    ca = float(request.GET['ca'])
    thal = float(request.GET['thal'])
    test = [[cp,ca,thal,oldpeak,age,chol,thalach,bps,sex]]
    ml = joblib.load('D:/Program/django/heart/heart/heart.joblib')
    # a = [name,age,sex,cp,bps,chol,thalach,oldpeak,ca,thal,test,ml]
    a = Heart_data(name=name,age=age,sex=sex,cp=cp,trestbps=bps,chol=chol,thalach=thalach,oldpeak=oldpeak,ca=ca,thal=thal,target=ml.predict(test))
    a.save()
    print(ml.predict(test))
    return render(request,'result.html',{'target':ml.predict(test)})

def example_data(request):
    query = Heart_data.objects.all()
    return render(request,'example.html',{'obj':query})