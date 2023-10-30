from django.shortcuts import render,get_object_or_404
from .models import product
from django.http import Http404
# Create your views here.
def product_list(request):
    products = product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request,product_id):
    
    return render(request, 'product/product_detail.html',{'product':product})