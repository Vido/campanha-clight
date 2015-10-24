from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="app/index.html"),name='index'),
    url(r'^cor/(?P<palavra>[a-z]+)/$', TemplateView.as_view(template_name="app/cor.html"),name='cor'),
]
