from django.shortcuts import render
from .models import Iris
from .form import IrisForm
# Create your views here.

def predict(request):

    form = IrisForm()
    return render(request,'predict.html',{'form':form})