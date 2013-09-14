

from django.db import models
from django.contrib.auth.models import User

from products.models import Products

class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	total = models.FloatField(default=0)
	active = models.BooleanField(default=True)
	products = models.ManyToManyField(Products, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.id)