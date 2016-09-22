from django.conf.urls import url
from django.contrib import admin
import agenda.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', agenda.views.index),
]
