from django.shortcuts import render

from app.models import Task
from .filters import *
# Create your views here.
def home(request):
    task =Task.objects.all()
    product = Product.objects.all()
    myfilter = ProductFilter(request.GET , queryset=product)
    product=myfilter.qs
    return render(request,('app/home.html'),context={'task':task,'product':product,'myfilter':myfilter})