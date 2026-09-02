from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You're in the Index.")

def post_list(request):
    return HttpResponse("")

def post_detail(request, pk):
    return HttpResponse("")
