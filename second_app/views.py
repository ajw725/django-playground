from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    view_data = {'dynamic_content': 'This is dynamic content!'}
    return render(request, 'second_app/index.html', view_data)


def pageone(request):
    view_data = {'dynamic_content': 'Welcome to page one'}
    return render(request, 'second_app/pageone.html', view_data)


def pagetwo(request):
    return HttpResponse('This is page two')
