from django.db import models

# Create your models here.

class housing(models.Model):
	adid = models.CharField(max_length=128)
	location = models.CharField(max_length=256)
	price = models.IntegerField()
	price_str = models.CharField(max_length=32)
	ad_url = models.CharField(max_length=256)
	bedroom = models.IntegerField()
	bath_s = models.IntegerField()
	bath_p = models.IntegerField()
	furniture = models.BooleanField()
	
	def __str__(self):
		return self.adid
	
