from django.db import models
import datetime

# Create your models here.
class Scrape(models.Model):
	created_on = models.DateTimeField(default=datetime.datetime.now)
	successful = models.BooleanField()