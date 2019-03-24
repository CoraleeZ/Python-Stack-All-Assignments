from django.shortcuts import render,redirect
from .models import books,authors
def index(request):
    context={
        'books':books.objects.all()
    }
    return render(request,'books_authors_app/bookadd.html',context)

def indexshow(request,idbook):
    c=books.objects.get(id=idbook)
    b=c.author.all()
    newlist={}
    for x in b:
        newlist[x.id]='r'
    newauthors=[]
    e=authors.objects.all()
    for y in e:
        if not y.id in newlist:
            newauthors.append(y)
        
    context={
        'books':books.objects.get(id=idbook),
        'author':newauthors
    }  
    return render(request,'books_authors_app/bookshow.html',context)

def addbooks(request):
    if request.method=='POST':
        books.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')


def addauthorforb(request,idbook):
    print(idbook)
    if request.method=='POST':
        c=books.objects.get(id=idbook)
        b=authors.objects.get(id=request.POST['select'])        
        c.author.add(b)
        print('success')
    return redirect('/books/'+str(idbook))


def authorsadd(request):
    context={
        'authors':authors.objects.all()
    }
    return render(request,'books_authors_app/authoradd.html',context)


def authorshow(request,idauthor):
    c=authors.objects.get(id=idauthor)
    b=c.book.all()
    newlist={}
    for x in b:
        newlist[x.id]='r'
    newbooks=[]
    e=books.objects.all()
    for y in e:
        if not y.id in newlist:
            newbooks.append(y)
        

    context={
        'authors':authors.objects.get(id=idauthor),
        'book':newbooks
    }  
    return render(request,'books_authors_app/authorshow.html',context)



def addauthors(request):
    if request.method=='POST':
        authors.objects.create(first_name=request.POST['fn'],last_name=request.POST['ln'],notes=request.POST['notes'])
    return redirect('/authors')


def addbookfora(request,idauthor):

    if request.method=='POST':
        c=authors.objects.get(id=idauthor)
        b=books.objects.get(id=request.POST['select'])        
        c.book.add(b)
        print('success')
    return redirect('/books/'+str(idauthor))


# Create your views here.
