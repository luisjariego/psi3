#!/usr/bin/env python
import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshop.settings')
import django 
django.setup()
from django.db import models
from django.core.files import File
from shop.models import Category, Product
from django.utils import timezone
from django.template.defaultfilters import slugify
import onlineshop.settings as settings	
def populate():
	# First, we will create lists of dictionaries containing the products
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.
	microwaves = [
		{"prodName": "TAURUS 970.930 READY, 700W, 20 L, 6 speeds, white",
		"prodSlug": "TAURUS_970.930",
		"image": "TAURUS_970.930.png",
		"description":"Equip your kitchen with Tauru's microwave oven Ready Grill. It will the most beloved tool in your household.",
		"price": 49.90,
		"stock": 1,
		"availability": True },
		{"prodName": "Taurus 970921000 LUXUS GRILL, 700W, Inox",
		"prodSlug": "TAURUS_970.921",
		"image": "TAURUS_970.921.png",
		"description":"A powerfull microwave with grill function",
		"price": 79,
		"stock": 2,
		"availability": True} ]
	washing_machines = [ ]
	refrigerators = [ ]
	vacuum_cleaners = [ ]
	cats = {"Microwave ovens": {"products": microwaves, "catSlug": "microwaves" },
		"Washing machines": {"products": washing_machines, "catSlug": "washing_machines" },
		"Refrigerators": {"products": refrigerators, "catSlug": "refrigerators" },
		"Vacuum cleaners": {"products": vacuum_cleaners, "catSlug": "vacuum_cleaners" } }

	# If you want to add more catergories or products,
	# add them to the dictionaries above.

	# The code below goes through the cats dictionary, then adds each category,
	# and then adds all the associated products for that category.
	# if you are using Python 2.x then use cats.iteritems() see
	# http://docs.quantifiedcode.com/python-anti-patterns/readability/
	# for more information about how to iterate over a dictionary properly.

	for cat, cat_data in cats.items():
		c = add_cat(cat)
		for p in cat_data["products"]:
			add_product(c, p["prodName"], p["prodSlug"], p["image"], p["description"], p["price"], p["stock"], p["availability"])
			# Print out the categories we have added.

	for c in Category.objects.all():
		for p in Product.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_product(cat, prodName, prodSlug, image, description, price, stock, availability, created, updated):
	imageObject = File(open(os.path.join("images", image),'r')) #From where we upload it
	p = Product.objects.get_or_create(category=cat, prodName=prodName, prodSlug=prodSlug)[0]
	p.image.save(image, imageObject, save= True)
	p.description=description
	p.price=price
	p.stock=stock
	p.availability=	availability
	p.save()
	return p
def add_cat(catName):
    c = Category.objects.get_or_create(catName=catName)[0]
    c.save()
    return c



# Start execution here!
if __name__ == '__main__':
    print("Starting onlineshop population script...")
populate()

