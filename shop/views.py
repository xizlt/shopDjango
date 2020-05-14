from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_POST

from .models import Product, Category
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    language = request.LANGUAGE_CODE

    # f = request.POST.get('filter_name')
    # if f:
    #     if f == 'dictsort_name':
    #         products = products.order_by('translations__name')
    #     elif f == 'dictsortreversed_name':
    #         products = products.order_by('-translations__name')
    #     elif f == 'dictsort_price':
    #         products = products.order_by('price')
    #     else:
    #         products = products.order_by('-price')
    #     return render(request, "shop/product/ajax_list.html", {'products': products})

    s = request.GET.get('s')
    search = ''
    if s:
        products = products.filter(
            Q(translations__language_code=language, translations__name__contains=s) |
            Q(translations__language_code=language, translations__description__contains=s)
        )
        search = f"s={s}&"

    if category_slug:
        category = get_object_or_404(Category, translations__language_code=language, translations__slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'page': page,
                   's': search,
                   })


def product_detail(request, id, slug):
    categories = Category.objects.all()
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, id=id, translations__language_code=language, translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'categories': categories})

