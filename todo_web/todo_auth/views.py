from django.shortcuts import render, redirect
from .forms import TaskCreator
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password




def signup_page(request):
    
    if request.method == 'POST':
        form = TaskCreator(request.POST)#to grab input data
        
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"hi {username} your account creation was a success")
            new_user = TaskCreator(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('todo_app:todo_list')
        
    else:
        print('user not registered')
        form = TaskCreator()


    context = {
        'form':form,

    }
    return render (request, 'todo_app/auth/sign-up.html', context)

def loginpage(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_app:todo_list')
        else:
            error_message = 'Invalid Username and Password'
            return render(request, 'todo_app/auth/login.html', {'error_message':error_message})

    return render(request, 'todo_app/auth/login.html')


def logoutpage(request):
    logout(request)
    messages.success(request, 'you have successfully logged out')
    return redirect('todo_auth:login')
# Create your views here.
