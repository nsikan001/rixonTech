from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("this is the home page")
    return render(request, 'index2.html', {})


def about(request):
    return HttpResponse("this is the about page")
