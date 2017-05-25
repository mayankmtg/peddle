from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Catagory, Offer
from django.shortcuts import render
import operator


def index(request):
	all_cats=Catagory.objects.all()
	top_deals=Offer.objects.order_by('-discount')[:4]


	context={
		'all_cats': all_cats,
		'top_deals': top_deals
	}
	
	return render(request, 'Home/index.html', context)


def detail(request, cat_id):
	catagory=get_object_or_404(Catagory, pk=cat_id)
	return render(request, 'Home/detail.html', { 'catagory' : catagory })
