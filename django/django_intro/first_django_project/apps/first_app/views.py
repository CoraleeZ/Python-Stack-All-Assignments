from django.shortcuts import render,HttpResponse,redirect

#first_app,/
def index(request):
    return HttpResponse('placeholder to display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a form to create a new blogs')


def create(request):
    return redirect('/')


def show(request,number):
    
    return HttpResponse('placeholder to display blog number:'+number)


def edit(request,number):
    return HttpResponse('placeholder to edit blog:'+number)
    
def destroy(request,number):
    return redirect('/')
# Create your views here.
