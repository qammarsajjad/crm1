from django.shortcuts import render


def home(request):
    return render (request,'acounts/dashboard.html')

def product(request):
    return render (request,'acounts/product.html')

def customer(request):
    return render (request,'acounts/customer.html')