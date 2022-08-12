from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt

import io
import urllib,base64


x=np.random.randint(10,100,100)
y=3*x+np.random.randint(10,100,100)

data={
    'one':'Home',
    'two':'town',
    'lst1':x,
    'lst2':y
}



plt.scatter(x,y, marker='+' ,color='r')
plt.savefig('C:/Users/admin/Documents/GitHub/Make_Your_Own_Plot_using_Django/static/fig2.png')


def allabout(request):
    return HttpResponse("hello Python")
    
def home(request):
   
    return render(request,"index.html",data)


def myform(request):
    res=0
    dta={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            res=n1+n2
            dta={
                'n1':n1,
                'n2':n2,
                'output':res
            }
    except:
        pass
    return render(request,"myform.html",dta)
