from django.db import models
from redditology.apps.scraper.models import Scrape

class Author(models.Model):
	name = models.TextField()

	def __unicode__(self):
		return self.name

class Snapshot(models.Model):
	created_on = models.DateTimeField()
	scrape = models.OneToOneField(Scrape, blank=True, null=True)

	def __unicode__(self):
		return 'Snapshot - ' + str(self.created_on)


class Subreddit(models.Model):
	name = models.TextField()

	def __unicode__(self):
		return self.name

class Domain(models.Model):
	name = models.TextField()

	def __unicode__(self):
		return self.name
	
class Post(models.Model):
	id = models.CharField(max_length=32, primary_key=True)
	title = models.TextField()
	url = models.URLField()
	over_18 = models.BooleanField()
	subreddit = models.ForeignKey(Subreddit)
	domain = models.ForeignKey(Domain)
	author = models.ForeignKey(Author)
	created_on_reddit = models.DateTimeField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class PostSnapshot(models.Model):
	num_comments = models.IntegerField()
	snapshot = models.ForeignKey(Snapshot)
	post = models.ForeignKey(Post)
	up_votes = models.IntegerField()
	down_votes = models.IntegerField()
	rank = models.IntegerField()

	@property
	def score(self):
		return (self.up_votes - self.down_votes)

	def __unicode__(self):
		return (str(self.post) + ' ' + str(self.snapshot))