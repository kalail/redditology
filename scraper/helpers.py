import datetime
from django.utils.timezone import utc


class PostParser(object):
	"""
	Wrapper for scraped posts. Exposes all post attributes.
	"""

	def __init__(self, raw_post, rank):
		self.post = raw_post['data']
		self.rank = rank

	@property
	def title(self):
		return self.post['title']

	@property
	def created_on(self):
		return datetime.datetime.utcfromtimestamp(self.post['created_utc']).replace(tzinfo=utc)

	@property
	def author(self):
		return self.post['author']

	@property
	def over_18(self):
		return self.post['over_18']

	@property
	def id(self):
		return self.post['id']

	@property
	def num_comments(self):
		return self.post['num_comments']

	@property
	def score(self):
		return self.post['score']

	@property
	def up_votes(self):
		return self.post['ups']

	@property
	def down_votes(self):
		return self.post['downs']

	@property
	def domain(self):
		return self.post['domain']
	
	@property
	def url(self):
		return self.post['url']

	@property
	def edited(self):
		return self.post['edited']

	@property
	def subreddit(self):
		return self.post['subreddit']