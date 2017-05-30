from django.db import models

class Catagory(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Product(models.Model):
	catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	price = models.CharField(max_length=250)
	img = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Offer(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	discount= models.IntegerField(default=0)

	def __str__(self):
		return self.product.name

#class Cart(models.Model):
