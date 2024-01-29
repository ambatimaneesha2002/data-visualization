from django.shortcuts import render
from . models import Product
from .models import  EnergyInsight
# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        "products":products
    }

    return render(request, 'chartapp/index.html',context)
def jon(request):
    energy= EnergyInsight.objects.all()

    context = {
        "energy":energy
    }

    return render(request, 'chartapp/index.html',context)
