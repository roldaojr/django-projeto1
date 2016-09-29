from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', listar, name='contato_listar'),
    url(r'adicionar$', adicionar, name='contato_adicionar'),
]
