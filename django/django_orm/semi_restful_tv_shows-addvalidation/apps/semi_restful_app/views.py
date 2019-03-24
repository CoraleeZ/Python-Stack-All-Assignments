from django.shortcuts import render,redirect
from .models import shows, networks
from django.contrib import messages

def new(request):
    return render(request,'semi_restful_app/new.html')

def create(request):
    if request.method=='POST':
        errors=shows.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value,extra_tags='red')
            return redirect('/shows/new')
        else:
            messages.success(request, "Successfully added!" ,extra_tags='green')
            a=networks.objects.filter(network_name=request.POST['net'])
            if a:
                r=networks.objects.get(network_name__exact=request.POST['net'])
                b=shows.objects.create(title=request.POST['ti'],release_date=request.POST['d'],desc=request.POST['des'],network=r)
            else:
                c=networks.objects.create(network_name=request.POST['net'])
                b=shows.objects.create(title=request.POST['ti'],release_date=request.POST['d'],desc=request.POST['des'],network=c)
        showid=b.id
        return redirect('/shows/'+str(showid))

def showinfo(request,showid):
    context={
        'info':shows.objects.get(id=showid)
    }
    return render(request,'semi_restful_app/tvshow.html',context)


def showall(request):
    context={
        'allinfo':shows.objects.all()
    }
    return render(request,'semi_restful_app/allshow.html',context)

def edit(request,editid):
  
    if request.method=='GET':
        context={
            'editinfo':shows.objects.get(id=editid)
        }
    return render(request,'semi_restful_app/edit.html',context)

def update(request,updateid):
    if request.method=='POST':
        errors=shows.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value,extra_tags='red')
            return redirect('/shows/'+updateid+'/edit')
        else:
            messages.success(request, "Successfully updated!" ,extra_tags='green')
            c=shows.objects.get(id=updateid)
            c.title=request.POST['ti']
            c.release_date=request.POST['d']
            c.desc=request.POST['des']
            c.save()
            a=networks.objects.filter(network_name=request.POST['net'])
            if a:
                c.network=networks.objects.get(network_name__exact=request.POST['net'])
                c.save()
            else:
                b=networks.objects.create(network_name=request.POST['net'])
                c.network=b
                c.save()

           
        return redirect('/shows/'+str(updateid))
    
def delete(request,deleteid):
    a=shows.objects.get(id=deleteid)
    a.delete()
    return redirect('/shows')




# Create your views here.
