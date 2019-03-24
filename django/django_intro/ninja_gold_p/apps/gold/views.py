from django.shortcuts import render,redirect,HttpResponse
import random,time

def index(request):
    if not 'score' in request.session:    
        request.session['score']=0
        request.session['act']=[]
        request.session['step']=0
    return render(request,'gold/ninjagole.html')


def process(request):

    if request.method=='POST':
        if request.POST['gold']=='farm':
            request.session['rfarm']=random.randint(10,20)
            request.session['farm']=request.session['rfarm']
            farm_str='<p style="color:green;">Earned '+str(request.session['rfarm'])+' golds from the farm! ('+time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
            request.session['act'].insert(0,farm_str)
        else:
            request.session['farm']=0

        if request.POST['gold']=='cave':
            request.session['rcave']=random.randint(5,10)
            request.session['cave']=request.session['rcave']
            cave_str='<p style="color:green;">Earned '+str(request.session['rcave'])+' golds from the cave! ('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
            request.session['act'].insert(0,cave_str)
        else:
            request.session['cave']=0

        if request.POST['gold']=='house':
            request.session['rhouse']=random.randint(2,5)
            request.session['house']=request.session['rhouse']
            house_str='<p style="color:green;">Earned '+str(request.session['rhouse'])+' golds from the house! ('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
            request.session['act'].insert(0,house_str)
        else:
            request.session['house']=0

        if request.POST['gold']=='casino':
            request.session['rcasino']=random.randint(-50,50)
            request.session['casino']=request.session['rcasino']
            if request.session['rcasino']<0:
                casino_str='<p style="color:red;">Entered a casino and lost '+str(request.session['rcasino'])+' golds...Ouch.('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
                request.session['act'].insert(0,casino_str)
            else:
                casino_str='<p style="color:green;">Earned '+str(request.session['rcasino'])+' golds from the casino! ('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
                request.session['act'].insert(0,casino_str)
        else:
            request.session['casino']=0

    request.session['score']+=request.session['farm']+request.session['cave']+request.session['house']+request.session['casino']
    request.session['step']+=1
    if request.session['step']<=15 and request.session['score']>=150:
        context={'step':'WIN'}
        return render(request,'gold/result.html',context)
    elif request.session['step']==15 and request.session['score']<150:
        context={'step':'LOSE'}
        return render(request,'gold/result.html',context)

    return redirect('/')



def clear(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
