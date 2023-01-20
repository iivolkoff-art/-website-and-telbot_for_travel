from django.shortcuts import render, redirect
from .models import Travel
from .forms import TravelForm

def index(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


    form = TravelForm()
    context = {
        'form': form
    }
    return render(request, 'travel/index.html', context)



