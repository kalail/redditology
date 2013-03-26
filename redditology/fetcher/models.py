from django.db import models
from django.utils import timezone


class Fetch(models.Model):
	"""Fetch

	A single attempt to fetch the latest front page posts on reddit.

	"""
	successful = models.NullBooleanField(default=None)
	created_on = models.DateTimeField(default=timezone.now)


class Snapshot(models.Model):
	fetch = models.ForeignKey(Fetch)
	rank = models.IntegerField()

	class Meta:
		abstract = True
