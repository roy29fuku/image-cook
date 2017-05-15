from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'recipes/', views.recipes, name='recipes'),
    url(r'^$', views.index, name='index'),
]
