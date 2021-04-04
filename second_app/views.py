from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import AccessRecord


def index(request):
    pages = AccessRecord.objects.order_by('date')
    ctx = {'access_records': pages}
    return render(request, 'second_app/index.html', context=ctx)


def pageone(request):
    view_data = {'dynamic_content': 'Welcome to page one'}
    return render(request, 'second_app/pageone.html', view_data)


def pagetwo(request):
    return HttpResponse('This is page two')
