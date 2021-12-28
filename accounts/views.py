from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            token = Token.objects.create(user=user)
            messages.success(request, f'Account created for successfully, check you email address for your access token!!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

