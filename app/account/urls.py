from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    # url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    # url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    # url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    # url(r'^new/$', views.new, name='new'),
]
