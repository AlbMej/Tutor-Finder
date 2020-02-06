from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import View

# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'templates/home.html', {
        'count': count
    })
