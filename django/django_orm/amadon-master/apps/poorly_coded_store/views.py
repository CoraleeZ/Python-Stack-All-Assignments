from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    a=Product.objects.get(id=request.POST["id"])
    price_from_form = float(a.price)
    total_charge = quantity_from_form * price_from_form
    Order.objects.create(quantity_ordered=request.POST["quantity"],total_price=total_charge)
    print("Charging credit card...")
    return redirect('/amadon/checkout')

def checkout(request):
    b=Order.objects.all()
    sum_quantity=0
    sum_pay=0
    for x in b:
        sum_quantity+=int(x.quantity_ordered)
        sum_pay+=int(x.total_price)


    a=Order.objects.last()
    context={
        'last':a,
        'sum_pay':sum_pay,
        'sum_quantity':sum_quantity
    }
    return render(request, "store/checkout.html",context)