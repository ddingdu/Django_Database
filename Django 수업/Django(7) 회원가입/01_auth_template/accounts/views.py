from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

def delete(request):
    # user = request.user
    # user.delete()
    request.user.delete()
    return redirect('articles:index')


def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form=PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/change_password.html', context)