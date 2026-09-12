from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404 , HttpResponseRedirect , HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CommentForm,PostForm
def index(request):
    posts = Post.published.all()[:3]
    selected_posts = Post.published.filter(selected=True)[:3]
    return render(request,'blog/index.html',context= {'selected_posts':selected_posts,'posts':posts})
def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post_list.html',context= {'posts':posts})
def post_detail(request,slug):
    post = get_object_or_404(Post.published,slug = slug)
    form = CommentForm()
    post_comments = post.comments.filter(post_status=True)

    return render(request,'blog/post_detail.html',context= {'post':post,'form':form,'comments':post_comments})
def about_us(request):
    return render(request,'blog/about_us.html')



@login_required
def post_comment(request,slug):
    post = get_object_or_404(Post.published, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(post=post,author=request.author,content = cd['content'],email=cd['email'],phone=cd['phone'])
            return redirect('blog:post_detail',slug=slug)
    else:
        form = CommentForm()
    return render(request,'forms/post_comment.html',{'form':form,'post':post})

@login_required
def create_post(request):
    post = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.author
            post.save()
            post.save()
    else:
        form = PostForm()
    return render (request,'forms/create_post.html',{'form':form,'post':post})



@login_required
def profile(request):
    published_posts = Post.published.filter(author=request.author)
    rejected_posts = Post.objects.filter(author=request.author,post_status='rejected')
    draft_posts = Post.objects.filter (author=request.author,post_status='draft')
    return render(request,'blog/profile.html',{ 'published_posts': published_posts, 'rejected_posts': rejected_posts, 'draft_posts': draft_posts})

