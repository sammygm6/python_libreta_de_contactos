from django.conf.urls import url
from . import views

urlpatterns = [
#/contacto/
    url(r'$', views.index, name='index'),
]
