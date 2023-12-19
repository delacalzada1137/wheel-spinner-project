
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse
from .models import Name
from .forms import NameForm
import random
import time

def pick_winner(request):

    names = Name.objects.all()


    if request.method == "POST":
        if names:
            time.sleep(2)
            winner = random.choice(names)
            return render(request, 'wheel_of_names/winner.html', {'winner': winner})
        else:
            return render(request, 'wheel_of_names/pick_winner.html', {'form': NameForm(), 'error_message': 'No names available to pick a winner.'})

    form = NameForm()
    return render(request, 'wheel_of_names/pick_winner.html', {'form': form})

def save_name_view(request):
    
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid:
            form.save()
            return render(reverse('pick_winner'))
        
    form = NameForm()
    return render(request, 'wheel_of_names/pick_winner.html', {'form': form})