from django.conf.urls import include, url
from . import views


app_name='Home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cat=(?P<cat_id>[0-9]+)/$', views.detail, name='detail'),
]
