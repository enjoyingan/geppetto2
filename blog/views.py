from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

def main(request):
    return render(request, 'main.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

# 제페토 되기 페이지
def be_geppetto(request):
    blogs = Blog.objects 
    blog_list = Blog.objects.all().order_by('-id') # 블로그 객체 최신순나열
    paginator = Paginator(blog_list, 2) # 3개씩 잘라내기
    page = request.GET.get('page') # 페이지 번호 알아오기
    posts = paginator.get_page(page) # 페이지 번호 인자로 넘겨주기
    return render(request, 'be/be_geppetto.html', {'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'be/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'be/new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.writer=request.user.username
    blog.name=request.user.profile.name
    blog.phone=request.user.profile.phone
    blog.age=request.GET['age']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/be_geppetto/'+str(blog.id))

def edit(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'be/edit.html',{'blog':blog})

def update(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    blog.title=request.GET['title']
    blog.writer=request.user.username
    blog.name=request.user.profile.name
    blog.phone=request.user.profile.phone
    blog.age=request.GET['age']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/be_geppetto/'+str(blog.id))

def delete(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('be_geppetto')