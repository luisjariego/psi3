# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Category, Product
from shop.forms import CategoryForm, ProductForm

# Create your views here.
def about(request):
    return render(request, 'shop/about.html')

def base(request):
	return render(request, 'shop/base.html');

#author: Luis Jariego
def product_list(request, catSlug=None):
	categories = Category.objects.all()
	try:
		category = Category.objects.get(catSlug = catSlug)
		products = Product.objects.filter(category = category)
	except Category.DoesNotExist:
		category = None
		products = Product.objects.all()
	return render(request, 'shop/list.html',
			{'category': category,
			 'categories': categories,
			 'products': products} )

#author: Luis Jariego
def product_detail(request, id, prodSlug):
	categories = Category.objects.all()
	product = Product.objects.get(id = id)
	return render(request, 'shop/detail.html', {'product': product, 'categories': categories, 'stock': range( product.stock +1)})


