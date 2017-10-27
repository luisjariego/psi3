# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    catName = models.CharField(max_length=128, unique=True)
    catSlug = models.SlugField(blank=True, unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category)
    prodName = models.CharField(max_length=128, unique=True)
    prodSlug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to = 'images/products')
    description = models.CharField(max_length=500)
    price = models.DecimalField( decimal_places = 2, max_digits = 8, default = 0) #??
    stock = models.IntegerField( default = 0) #??
    availability = models.BooleanField(default = True)
    created = models.DateTimeField(default = timezone.now) #??
    updated = models.DateTimeField(default = timezone.now) #??

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

