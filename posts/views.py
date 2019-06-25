from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
            form.user = request.user
            form.save()
            return redirect('home')
    return render(request, 'posts/create.html', {'form': form})

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/show.html', {"post": post})
    
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        photo = request.POST.get('photo')
        post.title = title
        post.content = content
        post.photo = photo
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/update.html', {"post": post})
    
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('home')
    
# Comment


def new_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/new_comment.html', {'post': post})
    
    
def create_comment(request, id):
    form = CommentForm()
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:show', post.id)
    return render(request, 'posts/new_comment.html', {'form': form})
        
        
def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post = comment.post
    comment.delete()
    return render(request, 'posts/show.html', {"post": post})
    

def favourite(request):
    user = request.user
    my_posts = user.likes.all()
    return render(request, 'posts/favourite.html', {'posts': my_posts})

   
def like(request, id):
    user = request.user #로그인한 유저를 가져옴
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        if post.likes.filter(id = user.id).exists(): #해당 post에 로그인한 유저가 like 컬럼에 존재하면
            post.likes.remove(user) #like 컬럼에서 해당 유저를 지운다.
        else:
            post.likes.add(user) #그 외의 경우 추가한다.
    return redirect('posts:show', post.id)    
        
