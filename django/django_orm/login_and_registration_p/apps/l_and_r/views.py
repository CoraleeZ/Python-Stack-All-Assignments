from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    pass
    return render(request,'l_and_r/lr.html')

def register(request):
    if request.method=='POST':
        errors=users.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value,extra_tags='red')
            return redirect('/')
        else:
            
            request.session['fn']=request.POST['fn']
            pwhash=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            users.objects.create(first_name=request.POST['fn'],last_name=request.POST['ln'],email=request.POST['em'],birthday=request.POST['birth'],password=pwhash)
        return redirect('/success')

def success(request):
    if 'fn' in request.session:
        if users.objects.filter(first_name=request.session['fn']):
            messages.success(request, "Successfully registered(or log in)!" ,extra_tags='green')
            context={
                'user':users.objects.last()
            }
            return render(request,'l_and_r/success.html',context)
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')

def logout(request):
    del request.session['fn']
    return redirect('/')

def login(request):
    if request.method=='POST':
        if users.objects.filter(email=request.POST['em']):
            a=users.objects.get(email=request.POST['em'])
            if bcrypt.checkpw(request.POST['pw'].encode(), a.password.encode()):
                request.session['fn']=a.first_name
                return redirect('/success') 
        else:
            messages.error(request,'Not valid! Try again!',extra_tags='red')
            return redirect('/')


# Create your views here.
