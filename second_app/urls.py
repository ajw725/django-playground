from django.urls import path
from second_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('one', views.pageone, name='page_one'),
    path('two', views.pagetwo, name='page_two'),
]
