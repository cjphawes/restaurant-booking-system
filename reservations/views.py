from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_reservation(request):
    return HttpResponse("This is my reservations app!")