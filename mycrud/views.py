from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def first(request):
    return render(request, 'mycrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'mycrud/funccrud.html', {'blogs':blogs})

def create(request):
    # 새로운 데이터를 저장하는 역할 == POST 형식
    if request.method == 'POST':
        #입력된 블로그 글들을 저장
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    # 글쓰기 페이지를 띄워주는 역할 == GET 형식(!POST)
    else:
        #단순히 입력받을 수 있는 form 띄우기
        form = NewBlog()
        return render(request, 'mycrud/new.html', {'form': form})

def update(request, pk):
    #어떤 블로그를 수정할지 해당하는 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    #해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance = blog)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'mycrud/new.html', {'form' : form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')