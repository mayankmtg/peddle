from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Catagory, Offer, Product
from django.shortcuts import render
from django.db.models import Q
import operator


def index(request):
	all_cats=Catagory.objects.all()
	top_deals=Offer.objects.order_by('-discount')[:4]


	context={
		'all_cats': all_cats,
		'top_deals': top_deals
	}
	
	return render(request, 'Home/index.html', context)


# def detail(request, cat_id):
# 	catagory=get_object_or_404(Catagory, pk=cat_id)
# 	return render(request, 'Home/detail.html', { 'catagory' : catagory })

def about(request):
	context={}
	return render(request, 'Home/about.html', context)
def contact(request):
	context={}
	return render(request, 'Home/contact.html', context)
def product(request, cat_name):
	all_cats=Catagory.objects.all()
	# print(cat_name)
	if cat_name == "all":
		prods=Product.objects.all()
	else:
		prods=Product.objects.filter(catagory__name=cat_name)

	context={
		'all_cats' : all_cats,
		'prods' : prods,
	}
	return render(request, 'Home/product.html', context)
def detail(request, prod_name):
	product=Product.objects.filter(name=prod_name)
	cat_prod=product.values('catagory')
	prods=Product.objects.filter(catagory__pk=cat_prod)
	if(len(prods) >4):
		prods=prods[:4]

	context={
		'product' : product[0],
		'cat_prod' : cat_prod,
		'prods' : prods,
	}
	return render(request, 'Home/detail.html', context)
def cart(request):
	context={}
	return render(request, 'Home/cart.html', context)