from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

def index(request):
    
    return render(request,'one/index.html')

def generate(request):
    request.session['count']=0
    if request.method=='GET':
        request.session['random']=get_random_string(length=14)
        request.session['count']+=1
    return redirect('random_word')

# Create your views here.
