from django.shortcuts import render
from .models import Board

# Create your views here.
def home(request):
    boards= Board.objects
    return render(request, 'home.html',{'boards':boards})