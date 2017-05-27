from django.conf.urls import include, url
from . import views


app_name='Home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^product/(?P<cat_name>\w+)/$', views.product, name='product'),
    url(r'^cat=(?P<cat_id>[0-9]+)/$', views.detail, name='detail'),
]
