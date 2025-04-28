from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'base.html')

import json
file=open(r'C:\Users\ambad\OneDrive\Desktop\django1\rentalcarproject\rentacar.json','r')
json_dat=file.read()
py_dat=json.loads(json_dat)
rental=py_dat["rental"]
def home(request):
    context={
        'rental':rental
    }
    return render(request,'home.html',context)
def one_item(request,id):
   context={
        'item':rental[id-1],
        
   } 
   return render(request,'show.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')