from django.shortcuts import render
from .forms import WineForm
from .ml_model import predict

def index(request):
    if request.method == 'POST':
        form = WineForm(request.POST)
        if form.is_valid():
            input_data = [form.cleaned_data[field] for field in form.cleaned_data]
            prediction = predict(input_data)[0]  # Ensure it returns the first element
            return render(request, 'mlapp/result.html', {'prediction': prediction})
    else:
        form = WineForm()
    
    return render(request, 'mlapp/index.html', {'form': form})
