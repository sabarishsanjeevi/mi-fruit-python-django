from django.shortcuts import render
from sklearn import tree
from .models import cld

# Create your views here.

def index(request):
    return render(request,'index.html')

def result(request):
    f = [['1','1','1'],['1','2','1'],['1','2','2'],['1','2','1'],['2','1','2'],['2','2','1'],['2','1','1'],['3','1','2'],['3','1','1'],['4','2','1'],['4','1','1'],['5','2','2'],['5','1','2'],['5','1','1'],['5','2','1'],['6','2','1'],['6','1','1'],['7','2','1'],['7','1','1'],['8','1','1'],['8','2','1'],['9','1','1'],['9','2','1']]

    l = ["Apple","Apple","Pomegranate","Pomegranate","Banana","Banana","Mango","Orange","Orange","Grapes","Grapes","Avacado","Avacado","Green Apple","Green Apple","Green Grapes","Green Grapes","Black Berry","Black Berry","Blue Berry","Blue Berry","Bosc Pears","Bosc Pears"]

    c = tree.DecisionTreeClassifier()

    c = c.fit(f,l)
    o = cld()
    a = int(request.POST.get("color"))
    b = int(request.POST.get("taste"))
    t = int(request.POST.get("surface"))

    d =c.predict([[a,b,t]])

    o.a = d[0]
    print(o.a)
    o.i = o.a.lower()+".png"
    print(o.i)

    return render(request,'result.html',{'a':o})