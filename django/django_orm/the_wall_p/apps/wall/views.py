from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime



def index(request):
    pass
    return render(request,'wall/lr.html')

def register(request):
    if request.method=='POST':
        errors=users.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value,extra_tags='red')
            return redirect('/')
        else:
            messages.success(request, "Successfully registered(or log in)!" ,extra_tags='green')
            request.session['fn']=request.POST['fn']
            pwhash=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            a=users.objects.create(first_name=request.POST['fn'],last_name=request.POST['ln'],email=request.POST['em'],password=pwhash)
            request.session['id']=a.id
        return redirect('/mainwall')

def mainwall(request):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                context={
                    'user':users.objects.get(id=request.session['id']),
                    'message':Messages.objects.all()
                }
                return render(request,'wall/mainwall.html',context)
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')

def logout(request):
    del request.session['fn']
    del request.session['id']
    return redirect('/')

def login(request):
    if request.method=='POST':
        if users.objects.filter(email=request.POST['em']):
            a=users.objects.get(email=request.POST['em'])
            if bcrypt.checkpw(request.POST['pw'].encode(), a.password.encode()):
                request.session['id']=a.id
                request.session['fn']=a.first_name
                messages.success(request, "Successfully registered(or log in)!" ,extra_tags='green')
                return redirect('/mainwall') 
        else:
            messages.error(request,'Not valid! Try again!',extra_tags='red')
            return redirect('/')


#wall
def addmessage(request):
    if request.method=='POST':
        a=users.objects.get(id=request.POST['userid'])
        Messages.objects.create(message=request.POST['message'],user=a)
        return redirect('/mainwall')

def wall(request):
    context={
        'user':users.objects.get(id=request.session['id']),
        'postm':Messages.objects.all()  
    }
    return render(request,'wall/wall.html',context)

def addcomment(request): 
    if request.method=='POST':
        a=users.objects.get(id=request.POST['commentwriter'])
        b=Messages.objects.get(id=request.POST['messageid'],)
        comments.objects.create(comment=request.POST['commnet'],user=a,message=b)
        return redirect('/wall')


def deletemessage(request,messageid):
    a=Messages.objects.get(id=messageid)

    if a.user.id==request.session['id']:
        
        time=datetime.datetime.now()-a.created_at.replace(tzinfo=None)
        limit=datetime.timedelta(minutes=30)
        if time>limit:
            messages.error(request,'you can not delete message posted 30 minutes ago!',extra_tags='red')
            return redirect('/wall')
        else:
    
        # b=datetime.datetime.now()
        # c=datetime.datetime.strptime(str(a.created_at),'%Y-%m-%d %H:%m:%S')
        # (b-c).minute
        # if (b-c).minute<30:
            a.delete()
            return redirect('/wall')
        # else:
        #     messages.error(request,'you can not delete message posted 30 minutes ago!',extra_tags='red')
        #     return redirect('/wall')
    else:
        messages.error(request,'you can only delete message belongs to you',extra_tags='red')
        return redirect('/wall')


def deletecomment(request,commentid):
    a=comments.objects.get(id=commentid)
    if a.user.id==request.session['id']:
        a.delete()
        return redirect('/wall')
    else:
        messages.error(request,'you can only delete comment belongs to you',extra_tags='red')
        return redirect('/wall')











# Create your views here.
