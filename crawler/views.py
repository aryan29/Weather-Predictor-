from django.shortcuts import render,redirect,reverse
from .forms import CustomForm
import requests
import json
cityname=""
def index(request):
    global cityname
    print("Cityname is ",cityname)
    url=f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=ca86a7f3fe70896527766f6c3cb0657a"
    dict=requests.get(url).json()
    #print("Url is ",url)
    #print("Dict is ",dict)
    mydict={
        'name':dict['name'],
        'temperature':dict['main']['temp'],
        'weather':dict['weather'][0]['description'],
        'icon':dict['weather'][0]['icon'],
        'description':dict['weather'][0]['description'],
    }
    print(mydict)
    return render(request,'base.html',mydict)
def lets(request):
    global cityname
    if(request.method=="POST"):
        form=CustomForm(request.POST)
        if form.is_valid():
            cityname=form['City'].value()
           # print("Form is ",form)
            #print("Cityname is ",cityname)
            return redirect('index')
    else:
        form=CustomForm()
    return render(request,'new.html',{'form':form})
# Create your views here.
