from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="app/index.html"),name='index'),
    url(r'^cor/(?P<palavra>[a-z]+)/$', views.cor,name='cor'),
    url(r'^compartilhe/(?P<palavra>[a-z]+)/$', views.compartilhe,name='compartilhe'),
]
