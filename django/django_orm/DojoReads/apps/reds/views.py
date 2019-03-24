from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime

def index(request):
    pass
    return render(request,'reds/lr.html')

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
            a=users.objects.create(first_name=request.POST['fn'],last_name=request.POST['ln'],email=request.POST['em'],password=pwhash)
            request.session['id']=a.id
        return redirect('/books')


def login(request):
    if request.method=='POST':
        if users.objects.filter(email=request.POST['em']):
            a=users.objects.get(email=request.POST['em'])
            if bcrypt.checkpw(request.POST['pw'].encode(), a.password.encode()):
                request.session['id']=a.id
                request.session['fn']=a.first_name
                messages.success(request, "Successfully registered(or log in)!" ,extra_tags='green')
                return redirect('/books') 
        else:
            messages.error(request,'Not valid! Try again!',extra_tags='red')
            return redirect('/')


def bookshome(request):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                 ####validate login###
                reverse_review=[]
                a=reviews.objects.all()
                for x in a:
                    reverse_review.insert(0,x)


                #########star
                for y in range(3):
                    star_x=[]
                    for x in range(int(reverse_review[y].rate)):
                        star_x.append(1)
                    reverse_review[y].__dict__['star']=star_x
                 ##############star end

                ####other books on the right list
                last_three_list={}
                for x in range(3):
                    last_three_list[reverse_review[x].book.book_name]=1
                other_books=[]
                e=books.objects.all()
                for y in e:
                    if not y.book_name in last_three_list:
                            other_books.append(y)
                  ################# 
                context={
                    'user':users.objects.get(id=request.session['id']),
                    'reviews':reverse_review[:3],
                    'otherbook':other_books
    
                }
                return render(request,'reds/book.html',context)
                 ####validate login###
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')

def logout(request):
    del request.session['fn']
    del request.session['id']
    return redirect('/')



def addbook(request):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                ####validate login###
                context={
                    'authorname':authors.objects.all()
                }
                return render(request,'reds/addbook.html',context)
                ####validate login###
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')
    



def addbookprocess(request):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                ####validate login###
                if request.method=='POST':
                    if 'an' and 'anexist' in request.POST:
                        messages.error(request,'re-enter author information please!',extra_tags='red')
                        return redirect('/books/add')
                    if 'an' in request.POST:
                        au=authors.objects.create(author_name=request.POST['an'])
                    if 'anexist' in request.POST:
                        au=authors.objects.get(id=request.POST['anexist'])
                    u=users.objects.get(id=request.session['id'])
                    b=books.objects.create(book_name=request.POST['bn'],user=u,author=au)
                    reviews.objects.create(review=request.POST['review'],rate=request.POST['rate'],book=b,user=u)
                    return redirect('/books/'+str(b.id))
                ####validate login###
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')
    



def booksinfo(request,bookid):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                ####validate login###
                context={
                    'user':users.objects.get(id=request.session['id']),
                    'books':books.objects.get(id=bookid)
                }
                return render(request,'reds/bookdetail.html',context)
                ####validate login###
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')
    
def reviewprocess(request,bookid_addreview):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                ####validate login###
                if request.method=='POST':
                    u=users.objects.get(id=request.session['id'])
                    b=books.objects.get(id=bookid_addreview)
                    reviews.objects.create(review=request.POST['review'],rate=request.POST['rate'],book=b,user=u)
                    return redirect('/books/'+str(bookid_addreview))
                ####validate login###
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')


def userinfo(request,userid):
    if 'id' in request.session and 'fn' in request.session:
        if users.objects.filter(id=request.session['id']):
            a=users.objects.get(id=request.session['id'])
            if a.first_name==request.session['fn']:
                ####validate login###
                a=users.objects.get(id=userid)
                context={
                    'user':a,
                    'num_re':len(a.review.all())
                }
                return render(request,'reds/userinfo.html',context)
                ####validate login###
    else:
        messages.error(request,'You are not log in yet!', extra_tags='red')
        return redirect('/')


# Create your views here.
