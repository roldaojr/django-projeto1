from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', listar, name='contato_listar'),
    url(r'adicionar$', adicionar, name='contato_adicionar'),
    url(r'alterar/(?P<pk>\d+)$', alterar, name='contato_alterar'),
    url(r'apagar/(?P<pk>\d+)$', apagar, name='contato_apagar'),
]
