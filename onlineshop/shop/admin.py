# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop.models import Category, Product

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url')

admin.site.register(Category)
admin.site.register(Product)
