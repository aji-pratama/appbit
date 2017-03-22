from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Product, Category, CategoryProduct
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'products/index.html')

def categories(request):
    try:
        categori_list = Category.objects.all()
        if request.POST:
            q = request.POST.get('q')
            categori_list = Category.objects.filter(title__contains=q)

        paginator = Paginator(categori_list, 5) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            categories = paginator.page(1)
        except EmptyPage:
            categories = paginator.page(paginator.num_pages)

    except Category.DoesNotExist:
        raise Http404("Category Does Not Exist")
    return render(request, 'categories/categories.html', {'categories': categories})

def create_category(request):
    if request.POST:
        title = request.POST.get('title')
        parent_id = request.POST.get('parent_id')

        if parent_id:
            create_category = Category(title=title, parent_id=parent_id)
        else:
            create_category = Category(title=title)
        create_category.save()

        return HttpResponseRedirect('/categories')

    categories = Category.objects.all()
    return render(request, 'categories/create.html', {'categories': categories})

def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    if request.POST:
        title = request.POST.get('title')
        parent_id = request.POST.get('parent_id')
        category.title = title
        category.parent_id = parent_id
        category.save()
        return HttpResponseRedirect('/categories')

    return render(request, 'categories/edit.html', {'category': category, 'categories': categories})

def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect('/categories')

#Products
def products(request):
    try:
        products = Product.objects.all()

    except Product.DoesNotExist:
        raise Http404("Product Does Not Exist")

    return render(request, 'categories/categories.html', {'products': products})
