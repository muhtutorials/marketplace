from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import UserSignupForm


def signup(request):
    next_page = request.GET.get('next')  # page to redirect to after registering (previous page)
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # save username and password to authenticate and login user automatically after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account with username "{username}" has been created')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_page)
            else:
                return HttpResponse('User does not exist')

    else:
        form = UserSignupForm()

    return render(request, 'registration/signup.html', {'form': form})
