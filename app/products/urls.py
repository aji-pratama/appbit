from django.conf.urls import url
from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Category
    url(r'^categories$', views.categories, name='categories'),
    url(r'^categories/create', views.create_category, name='create_category'),


    #Product
    url(r'^products', views.products, name='products'),
]
