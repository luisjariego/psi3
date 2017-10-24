# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Category, Product
from shop.forms import CategoryForm, ProductForm

# Create your views here.

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects#.order_by('catName')[:5]
    product_list = Product.objects#.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'products': product_list }
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	
    return render(request, 'shop/index.html', context=context_dict)

def about(request):
    return render(request, 'shop/about.html')

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass 
    # to the template rendering engine.
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        products = Product.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['products'] = pages
        # We also add the category object from 
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - 
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['products'] = None
    
    # Go render the response and return it to the client.
    return render(request, 'shop/category.html', context_dict)

def add_category(request):
    form = CategoryForm()
    
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
			cat = form.save(commit=True)
			print(cat, cat.slug)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
			return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'shop/add_category.html', {'form': form})

def add_product(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            if category:
                product = form.save(commit=False)
                product.category = category
                product.stock = 1
                product.availability = True
                product.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    
    context_dict = {'form':form, 'category': category}
    return render(request, 'shop/add_product.html', context_dict)

