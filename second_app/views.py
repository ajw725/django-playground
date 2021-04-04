from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import AccessRecord, User
from . import forms


def index(request):
    pages = AccessRecord.objects.order_by('date')
    ctx = {'access_records': pages}
    return render(request, 'second_app/index.html', context=ctx)


def users(request):
    form = forms.UserForm

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('User created!')
            return index(request)

    ctx = {'form': form}
    return render(request, 'second_app/users.html', context=ctx)


def pageone(request):
    view_data = {'dynamic_content': 'Welcome to page one'}
    return render(request, 'second_app/pageone.html', view_data)


def pagetwo(request):
    return HttpResponse('This is page two')
