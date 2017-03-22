from django.conf.urls import url
from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Category
    url(r'^categories$', views.categories, name='categories'),
    url(r'^categories/create', views.create_category, name='category_create'),
    url(r'^categories/edit/(?P<pk>\d+)$', views.category_edit, name='category_edit'),
    url(r'^categories/delete/(?P<pk>\d+)$', views.category_delete, name='category_delete'),

    #Product
    url(r'^products', views.products, name='products'),
]
