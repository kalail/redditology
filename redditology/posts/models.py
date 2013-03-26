from django.db import models
from django.utils import timezone
from fetcher.models import Snapshot

# class Author(models.Model):
# 	name = models.TextField()

# 	def __unicode__(self):
# 		return self.name


# class Subreddit(models.Model):
# 	name = models.TextField()

# 	def __unicode__(self):
# 		return self.name


# class Domain(models.Model):
# 	name = models.TextField()

# 	def __unicode__(self):
# 		return self.name


class Post(models.Model):
	id = models.CharField(max_length=32, primary_key=True)
	title = models.TextField()
	url = models.URLField()
	over_18 = models.BooleanField()
	subreddit = models.CharField(max_length=512)
	domain = models.CharField(max_length=256)
	author = models.CharField(max_length=128)
	created_on_reddit = models.DateTimeField()
	created_on = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.title


class PostSnapshot(Snapshot):
	post = models.ForeignKey(Post)
	num_comments = models.IntegerField()
	up_votes = models.IntegerField()
	down_votes = models.IntegerField()

	@property
	def score(self):
		return (self.up_votes - self.down_votes)

	def __unicode__(self):
		return '%s - %s' % (self.post, self.fetch)