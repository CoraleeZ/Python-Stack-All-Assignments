from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    if not 'random' in request.session:
        request.session['random']=get_random_string(length=14)
    return render(request,'random_word/index.html')

def generate(request):

    if request.method=='GET':
        request.session['count']+=1
        request.session['random']=get_random_string(length=14)
    return redirect('/random_word')

def delete(request):
    del request.session['count']
    del request.session['random']
    return redirect('/random_word')

# Create your views here.
