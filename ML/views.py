from django.shortcuts import render
from .models import Iris
from .forms import IrisForm
import pandas as pd

def predict(request):

    if request.method == 'POST':
        form = IrisForm(request.POST)
        if form.is_valid():
            print("Form is valid")

            cleaned_data = form.cleaned_data
            sepal_length = cleaned_data['sepal_length']
            sepal_width = cleaned_data['sepal_width']
            petal_length = cleaned_data['petal_length']
            petal_width = cleaned_data['petal_width']

            # Prediction التنبئو
            model = pd.read_pickle("model.pickle")
            result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

            # List prop[]
            classifiction = result[0]

            # Save
            myform = form.save(commit=False)
            myform.classifiction = classifiction
            myform.save()
            return render(request,'predict.html',{'result': classifiction})
        else:
            print("Form is not valid")
            print(form.errors)

    else:
        form = IrisForm()

    return render(request, 'predict.html', {'form': form})



from rest_framework import generics
from rest_framework.response import Response

class PredictAPI(generics.CreateAPIView):
    def post(self,request,**kwargs): 
        sepal_length = request.data['sepal_length']
        sepal_width = request.data['sepal_width']
        petal_length = request.data['petal_length']
        petal_width = request.data['petal_width']

        model = pd.read_pickle("model.pickle")
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        # List prop[]
        classification = result[0]

        Iris.objects.create(
            sepal_length=sepal_length
            , sepal_width = sepal_width
            , petal_length= petal_length
            , petal_width= petal_width,
              classifiction=classification 
        )
        return Response({'class':classification})