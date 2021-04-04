from django.shortcuts import render
from django import forms
from users.models import User
from . import forms

# Create your views here.


def index(request):
    users_list = User.objects.order_by('last_name', 'first_name')
    ctx = {'users': users_list, 'text': 'remove hi me hi'}
    return render(request, 'users/index.html', context=ctx)


def new(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('User created!')
            return index(request)

    ctx = {'form': form}
    return render(request, 'users/new.html', context=ctx)
