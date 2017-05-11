from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'books/', views.books, name='books'),
    url(r'^$', views.index, name='index'),
]
