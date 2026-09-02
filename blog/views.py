from django.shortcuts import render
from .models import *
from django.http import HttpResponse,Http404,HttpResponseNotFound, HttpResponseRedirect,HttpResponseNotAllowed
def index(request):
    selected_posts = Post.published.filter(selected=True)
    return render(request,'blog/index.html',{'selected_posts':selected_posts})
def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post_list.html',{'posts':posts})
def post_detail(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        raise Http404
    return render(request,'blog/post_detail.html',{'post':post})
def about_us(request):
    return render(request,'blog/about_us.html',)
