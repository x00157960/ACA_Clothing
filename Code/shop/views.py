from django.shortcuts import render, get_object_or_404, redirect

from django.db.models import Count
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def SignupView(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customers')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})

def SigninView(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('cart')
            else:
                return redirect('signup')
    else:
        form =AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form })

def SignoutView(request):
    logout(request)
    return redirect('cart')
