import praw
import pytz
from celery.utils.log import get_task_logger
from django.core.cache import cache
from celery.task import task
from datetime import datetime
from posts.models import Post, PostSnapshot
from .models import Fetch


logger = get_task_logger(__name__)

class post_object(object):
	pass


@task
def fetch_posts():
	"""Fetch Posts

	Fetch the current top 100 posts on the reddit homepage using the PRAW package and then dispatch the tasks to save the posts.

	"""
	logger.info('Fetching front page posts')
	reddit = praw.Reddit(user_agent='Redditology - Front Page Posts Fetcher')
	# Fetch posts
	fetch = Fetch.objects.create()
	try:
		posts = reddit.get_front_page(limit=100)
	except Exception:
		logger.error('Error fetching posts!')
		fetch.successful = False
	else:
		logger.info('Done')
		fetch.successful = True
	finally:
			fetch.save()
	# Exit if failed
	if not fetch.successful:
		return
	# import pdb; pdb.set_trace()
	logger.info('Dispatching save tasks')
	for idx, post in enumerate(posts):
		# Correct rank offset
		rank = idx + 1

		# Bug in requests prevents pickling post. Create p as proxy object.
		p = post_object()
		p.id = post.id
		p.title = post.title
		p.author = post.author.name
		p.url = post.url
		p.domain = post.domain
		p.over_18 = post.over_18
		p.subreddit = post.subreddit.display_name
		p.num_comments = post.num_comments
		p.created_utc = post.created_utc
		p.ups = post.ups
		p.downs = post.downs
		
		post_cache_key = 'fetched_post_%s' % (p.id)
		cache.set(post_cache_key, p)

		save_fetched_post.delay(post_cache_key, rank,  fetch.id)
		logger.info('Sent rank %s post task' % rank)


@task
def save_fetched_post(post_cache_key, rank, fetch_id):
	"""Save Fetched Post

	Extracts fetched post from the cache to update the post properties and create snapshots of time varying post data in the database.

	"""
	# Get post from cache
	post = cache.get(post_cache_key, None)

	# Check for existence
	if not post:
		logger.error('Post not in cache')
		return

	# Consume post
	cache.delete(post_cache_key)

	# Get or create post model
	try:
		p = Post.objects.get(id=post.id)
	except Post.DoesNotExist:
		p = Post(id=post.id)
	# Update all fields
	p.title = post.title
	p.author = post.author
	p.url = post.url
	p.domain = post.domain
	p.over_18 = post.over_18
	p.subreddit = post.subreddit
	p.created_on_reddit = datetime.utcfromtimestamp(post.created_utc).replace(tzinfo=pytz.UTC)
	p.save()

	fetch = Fetch.objects.get(id=fetch_id)

	post_snapshot = PostSnapshot(
		# Relations
		post = p,
		fetch = fetch,
		# Time data
		up_votes = post.ups,
		down_votes = post.downs,
		rank = rank,
		num_comments = post.num_comments
	)
	post_snapshot.save()
