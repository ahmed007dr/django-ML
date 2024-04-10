from django.shortcuts import render
from .models import Iris
from .form import IrisForm
import pandas as pd

def predict(request):

    if request.method == 'POST':
        form = IrisForm(request.POST)
        if form.is_valid():

            cleaned_data = form.cleaned_data
            sepal_length = cleaned_data['sepal_length']
            sepal_width = cleaned_data['sepal_width']
            petal_length = cleaned_data['petal_length']
            petal_width = cleaned_data['petal_width']

            # Prediction التنبئو
            model = pd.read_pickle("model.pickle")
            result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

            # List prop[]
            classification = result[0]

            # Save
            myform = form.save(commit=False)
            myform.classification = classification
            myform.save()
            return render(request,'predict.html',{'result': classification})
    else:
        form = IrisForm()

    return render(request, 'predict.html', {'form': form})
