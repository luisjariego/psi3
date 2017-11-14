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
		"availability": True},
		{"prodName": "Samsung GE731 K microwave",
		"prodSlug": "Samsung_GE731_K",
		"image": "Samsung_GE731_K.jpeg",
		"description":"Our most modern microwave.",
		"price": 73.39,
		"stock": 9,
		"availability": True},
		{"prodName": "Whirlpool AMW 160/IX 900W, Grill function 1000W",
		"image": "Whirlpool_AMW160.png",
		"description":"An integrable microwave.",
		"price": 221,
		"stock": 7,
		"availability": True},
		{"prodName": "Samsung MS11K3000AS 1.1 cu. ft. Countertop Microwave ",
		"image": "Samsung_MS11_Microwave.jpg",
		"description":"Microwave Oven with Sensor and Ceramic Enamel Interior, Silver Sand.",
		"price": 121,
		"stock": 2,
		"availability": True},
		{"prodName": "Hamilton Beach 0.9 cu ft 900W Microwave",
		"image": "Hamilton_900W_Microwave.jpg",
		"description":"10 microwave power levels / 1-touch cooking features: popcorn, potato, reheat, frozen dinner, beverage and pizza.",
		"price": 66,
		"stock": 49,
		"availability": True}
		 ]
	washing_machines = [
		{"prodName": "Bosch WAQ 28468, 8kg, 1400rpm, LCD Display, A+++",
		"prodSlug": "BOSCH_WAQ28468",
		"image": "BOSCH_WAQ28468.png",
		"description":"New exterior structure, specially made to be more silent.",
		"price": 389,
		"stock": 7,
		"availability": True},
		{"prodName": "Beko WTE6511BW, 39L, 6KG, 1000 R.P.M, A+++",
		"prodSlug": "Beko_WTE6511BW",
		"image": "Beko_WTE6511BW.png",
		"description":"Get impecable results in all your clothes.",
		"price": 219,
		"stock": 5,
		"availability": True},
		{"prodName": "Balay 3TS976BA 7Kg, 1200 rpm, A+++",
		"prodSlug": "Balay_3TS976BA",
		"image": "Balay_3TS976BA.png",
		"description":"Clean up!",
		"price": 295,
		"stock": 2,
		"availability": True},
		{"prodName": "Siemens WM14Q468ES, 8kg, 1400rpm, Digital display, A+++",
		"prodSlug": "Siemens_WM14Q468ES",
		"image": "Siemens_WM14Q468ES.png",
		"description":"Buy it!",
		"price": 398,
		"stock": 0,
		"availability": False},
		{"prodName": "Kenmore 28132 5.3 cu. ft. Top Load Washer in White",
		"prodSlug": "",
		"image": "Kenmore_28132.jpg",
		"description":"The Deep Fill option automatically adjusts the water levels depending on load size, optimizing water usage",
		"price": 198,
		"stock": 36,
		"availability": True},
		{"prodName": "Kenmore Elite 51993 Wide Pedestal Washer",
		"prodSlug": "",
		"image": "Kenmore_Elite_51993.jpg",
		"description":"Wash two loads at the same time with the pedestal that's also a washer. 1 cubic foot capacity is perfect for intimates and hand-wash items",
		"price": 488,
		"stock": 0,
		"availability": False} ]
	refrigerators = [ 
		{"prodName": "Samsung Refrigerator in Stainless Steel",
		"image": "stainless-steel-samsung.jpg",
		"description":"CoolSelect Pantry provides added temperature control. High-Efficiency LED Lighting helps you quickly spot what you want",
		"price": 998,
		"stock": 5,
		"availability": True},
		{"prodName": "Frigidaire Refrigerator in Black Stainless Steel",
		"image": "Tblack-stainless-steel-frigidaire.jpg",
		"description":"Practical has never looked so stylish with Black Stainless Steel. Corner to corner LED lighting for better visibility",
		"price": 1298,
		"stock": 0,
		"availability": False},
		{"prodName": "American fridge - Samsung RS7528THCSL A++, Display, Inox",
		"image": "SAMSUNG_RS7528THCSL.png",
		"description":"Best design, with digital inverter compressor that ensures an optimal and silent functioning.",
		"price": 999,
		"stock": 4,
		"availability": True},
		{"prodName": "Balay fridge 3FC1601B 186cm, A++, LEDs",
		"image": "BALAY_3FC1601B.png",
		"description":"The perfect ally to fit all your products.",
		"price": 475,
		"stock": 2,
		"availability": True},
		{"prodName": "Danby 120 Can Beverage Center",
		"image": "Danby_120_refrigerator.jpg",
		"description":"Recessed side mount door handle and integrated lock with key. Tempered glass door with stainless steel trim and black body ",
		"price": 233,
		"stock": 25,
		"availability": True},
		{"prodName": "Della Mini Compact Refrigerator Freezer, White",
		"image": "Della_Mini_Refrigerator.jpg",
		"description":"Adjustable shelf in the refrigerator can be configured to help you stay organized and fit taller items when needed.",
		"price": 225,
		"stock": 78,
		"availability": True}]
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
			add_product(c, p["prodName"], p["image"], p["description"], p["price"], p["stock"], p["availability"])
			# Print out the categories we have added.

	for c in Category.objects.all():
		for p in Product.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_product(cat, prodName, image, description, price, stock, availability):
	try:
	     p = Product.objects.get(prodName=prodName)
	except Product.DoesNotExist:
		imageObject = File(open(os.path.join("images/", image),'r')) #From where we upload it
		p = Product.objects.create(category=cat, prodName=prodName)
		p.image.save("""%s/%s"""%(cat.catSlug, image), imageObject, save= True)
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

