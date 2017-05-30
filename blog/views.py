from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from .forms import UserLoginForm,RegisterUserForm
from django.utils import timezone
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import User

def delete_post_view(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        post.delete()
        return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/delete_post.html', {'post': post})
    

         

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        uname = request.POST['username']
        pswd = request.POST['password']
        email = request.POST['email']
        print("@@@@2",uname,pswd,email)
        if form.is_valid():
            user = User.objects.create_user(str(uname),str(email),str(pswd))
            user.save()
            print("!!!!!!!!!!!!",user)
            return redirect('login')
    else:
        form = RegisterUserForm()
        return render(request, 'blog/register_user.html', {'form':form})
 

    
def logout_view(request):
    logout(request)
    return redirect('login')
    print("logout succesfull")
    
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        print("2222",form)
        uname = form.cleaned_data.get("username")
        pswd = form.cleaned_data.get("password")
        
        if form.is_valid():
            user = authenticate(username=uname, password=pswd)

            if user is not None:
                login(request,user)
                return redirect('post_list')
            else:
                print("error inlogin")
                
            
    else:
        form = UserLoginForm()
        print("1111111",form)
        return render(request,'blog/new_login.html',{"form":form})
            
# def login_view(request):
#     form = UserLoginForm()
#     print("formmmmmm",form)
#     if form.is_valid():
# #        username = form.cleaned_date.get("username")
#   #      password = form.cleaned_date.get("password")
# #        user = User.objects.create_user(username,email,password)
#  #       user.save()
#         print("@@@@@",request)
#         user = authenticate(username=request.username, password=request.password)
#         if user is not None:
#             return redirect('post_list')
#         else:
#             print("error inlogin")
#     return render(request,'blog/new_login.html',{"form":form})

    
def post_list(request):
    posts = Post.objects.all()
    print("Posts@@@@@@2",posts)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print("formmmmmmm",form)
        print("parameter",request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        print("form response",form)
        return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
