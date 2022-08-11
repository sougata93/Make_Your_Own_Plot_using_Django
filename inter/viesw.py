from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt

import io
import urllib,base64




data={
    'one':'Home',
    'two':'town',
    'lst':[1,2,3,4,5],
    'rand':np.random.randint(1,10,23)
}

x=np.random.randint(1,10,100)
y=np.random.randint(1,10,100)

plt.scatter(x,y, marker='+' ,color='r')
plt.savefig('C:/Users/souga/Documents/dj/inter/static/fig1.png')


def allabout(request):
    return HttpResponse("hello Python")
    
def home(request):
   
    return render(request,"index.html",data)