from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Product, Category, CategoryProduct
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

#BUG: will change to dashboard or similiar names id:34
def index(request):
    return render(request, 'products/index.html')

#BUG: will change to categori_list id:33
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

#DONE: create flash message if created id:26
#BUG: should change to Category_create id:43
def create_category(request):
    if request.POST:
        title = request.POST.get('title')
        parent_id = request.POST.get('parent_id')

        if parent_id:
            create_category = Category(title=title, parent_id=parent_id)
        else:
            create_category = Category(title=title)
        create_category.save()

        messages.add_message(request, messages.INFO, 'Category %s added' % title)
        return redirect('/categories')

    categories = Category.objects.all()
    return render(request, 'categories/create.html', {'categories': categories})

#DONE: create flash message if changed id:25
def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    if request.POST:
        title = request.POST.get('title')
        parent_id = request.POST.get('parent_id')
        category.title = title
        category.parent_id = parent_id
        category.save()
        messages.add_message(request, messages.INFO, 'Category changed to %s ' % title)
        return HttpResponseRedirect('/categories')

    return render(request, 'categories/edit.html', {'category': category, 'categories': categories})

#DONE: create flash message if deleted id:24
#BUG: Deleted parent_id if id parent Deleted & message deleted color id:23
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    messages.add_message(request, messages.INFO, 'Category %s deleted' % category.title)
    category.delete()
    return HttpResponseRedirect('/categories')

#Products
#TODO: List Products id:28
def product_list(request):
    try:
        products = Product.objects.all()

    except Product.DoesNotExist:
        raise Http404("Product Does Not Exist")

    return render(request, 'categories/categories.html', {'products': products})

#TODO: create products id:29
def product_create(request):
    pass

#TODO: edit products id:31
def product_edit(request):
    pass

#TODO: delete products id:32
def product_delete(request):
    pass
